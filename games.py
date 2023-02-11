from app import app
from db import db
from flask import session, render_template
# import ???
from sqlalchemy.sql import text
from random import shuffle

game_id         = 0
question_list   = []
question_id     = 0
sessions        = 1
answers         = 0
points          = 0

# Identification number of the game
def game_id():
    global game_id
    return game_id

# Amount of points in the game
def game_points():
    global points
    return points

# Amount of submitted answers in the game
def game_answers():
    global answers
    return answers

# Amount of visited game sessions in the game
def game_sessions():
    global sessions
    return sessions

# Question category of the game
def game_category():
    return session.get("game_category", 0)

# Question level of the game
def game_level():
    return session.get("game_level", 0)

# Visibility of the game: True = active, False = inactive
def game_visible():
    return session.get("game_visible", False)

# Date and time when the game has been created
def game_created():
    return session.get("game_created", None)
    
def question_id():
    global question_id
    return question_id

def question_text():
    return session.get("question_text", "")

def question_category():
    return session.get("question_category", 0)

def question_level():
    return session.get("question_level", 0)

def question_visible():
    return session.get("question_visible", False)
    
def question_amount():
    global question_list
    return len(question_list)

def answer_right():
    return session.get("answer_right", 0)

def is_right(answer):
    return answer == session.get("answer_right", 0)

# Get answer information
def get_answer(id):
    sql = """SELECT id, answer, correct, visible
        FROM answers WHERE id=:id"""
    result = db.session.execute(text(sql), {"id":id})
    answer = result.fetchone()
    return answer
    
# Get questions of selected category & level -> query returns list of selected questions with all info
def get_questions(category_id, level_id):
    global question_list
    empty_session_questions()
    question_list   = []
    visible         = "TRUE"

    sql = """SELECT id, question, category_id, level_id, visible 
        FROM questions WHERE category_id=:category_id AND level_id=:level_id AND visible=:visible """
    result = db.session.execute(text(sql), {"category_id":category_id, "level_id":level_id, "visible":visible})
    question_list = list(result.fetchall())
    shuffle(question_list)

    return question_list

# Get answer alternatives (right and wrong) by question id -> returns the right answer 
# and stores all answers to session variables
def get_answers(question_id):

    sql = """SELECT answer_id 
        FROM questions_answers WHERE question_id=:question_id"""
    result = db.session.execute(text(sql), {"question_id":question_id})
    answer_ids = result.fetchall()

    i_list = [0,1,2]
    shuffle(i_list)
    answer_1 = get_answer(answer_ids[i_list[0]][0])
    answer_2 = get_answer(answer_ids[i_list[1]][0])
    answer_3 = get_answer(answer_ids[i_list[2]][0])

    session["answer_text_1"] = answer_1.answer
    session["answer_text_2"] = answer_2.answer
    session["answer_text_3"] = answer_3.answer
    
    right_answer = 0
    session["answer_correct_1"] = answer_1.correct
    if answer_1.correct: right_answer = 1
    session["answer_correct_2"] = answer_2.correct
    if answer_2.correct: right_answer = 2
    session["answer_correct_3"] = answer_3.correct
    if answer_3.correct: right_answer = 3

    session["answer_right"] = right_answer

    return right_answer

# Delete session variables related to current question    
def empty_session_questions():
    if question_text() != "":
        del session["question_text"]
    if question_category() in (1, 2, 3, 4, 5, 6):
        del session["question_category"]
    if question_level() in (1, 2, 3):
        del session["question_level"]
    if question_visible() == True:
        del session["question_visible"]

# Delete session variables related to current answers
def empty_session_answers():
    if session["answer_text_1"] != "":
        del session["answer_text_1"]
    if session["answer_text_2"] != "":
        del session["answer_text_2"]
    if session["answer_text_3"] != "":
        del session["answer_text_3"]

    if session["answer_correct_1"] != "":
        del session["answer_correct_1"]
    if session["answer_correct_2"] != "":
        del session["answer_correct_2"]
    if session["answer_correct_3"] != "":
        del session["answer_correct_3"]

    if answer_right() != "":
        del session["answer_right"]

# Get the following question to game from the question list 
# -> returns question id and length of question list in tuple     
def get_new_question():
    global game_id
    global question_list
    global question_id

    # Choose first question from the list,
    # and drop the fetched question from question list, if list is not empty
    if len(question_list) < 1 or question_list == None:
        return False
    question = question_list[0]
    question_list = question_list[1:len(question_list)]

    session["question_id"]      = question[0]
    session["question_text"]    = question[1]
    session["question_category"]= question[2]
    session["question_level"]   = question[3]
    session["question_visible"] = question[4]

    question_id = question[0]

    try:     	
        sql = """INSERT INTO games_questions (game_id, question_id) VALUES (:game_id, :question_id)"""
        db.session.execute(text(sql), {"game_id":game_id, "question_id":question_id})       
        db.session.commit()
    except:
        return False

    return (question.id, len(question_list))

# Setup the game info to database and game session variables    
def set_game_attr(user_id, category_id, level_id):
    global sessions
    global answers
    global points
    global game_id
    try:     	
        sql = """INSERT INTO games (user_id, category_id, level_id) 
        VALUES (:user_id, :category_id, :level_id)
        RETURNING id, user_id, points, answers_count, session_count, category_id, level_id, visible, created_at"""
        result = db.session.execute(text(sql), {"user_id":user_id, "category_id":category_id, "level_id":level_id})       
        game = result.fetchone()
        db.session.commit()

        session["game_id"] 		= game.id
        session["game_user"] 		= game.user_id
        session["game_points"] 		= game.points
        session["game_answers"] 	= game.answers_count
        session["game_sessions"]	= game.session_count
        session["game_category"] 	= game.category_id
        session["game_level"] 		= game.level_id
        session["game_visible"]     	= game.visible
        session["game_created"] 	= game.created_at

        sessions    = game.session_count
        answers     = game.answers_count
        points      = game.points

        game_id = game.id
        return game.id
    except:
        return 0

# Creates new game with user id, category id and level id 
# -> returns game id (by calling first "get_game_id" function)
def create_game(user_id, category_id, level_id):

    # Get the right question set (of chosen category and level) to the game
    questions = get_questions(category, level)
    
    if len(questions) < 1:
        return False
        
    gid = set_game_attr(user, category, level)
    return gid, list(questions)    
    
# Ask a question and handle the received answer  
def play():
    global sessions
    sessions += 1
    q_details       = get_new_question()
    if not q_details:
        return False
    qid             = q_details[0]
    question_amount = q_details[1]
    if not qid:
        return False
    session["question_id"] = qid
    get_answers(qid)
    return question_amount

# Gather game statistics
def continue_game(right):
    global answers
    global points
    global question_id
    answers += 1
    # Add answer count and points, if right answer
    if right: points += 1
    
    session["game_points"]  = points
    session["game_answers"] = answers