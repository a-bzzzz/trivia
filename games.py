from app import app
from db import db
from flask import session, render_template
# import ???
from sqlalchemy.sql import text

# Identification number of the game
def game_id():
    return session.get("game_id", 0)

# Amount of points in the game
def game_points():
    return session.get("game_points", 0)

# Amount of submitted answers in the game
def game_answers():
    return session.get("game_answers", 0)

# Amount of visited game sessions in the game
def game_sessions():
    return session.get("game_sessions", 0)

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

# Create a game with user id, category id and level id
def create_game(user_id, category_id, level_id):

    try:
        sql = """INSERT INTO games (user_id, category_id, level_id) VALUES (:user_id, :category_id, :level_id)"""
        db.session.execute(text(sql), {"user_id":user_id, "category_id":category_id, "level_id":level_id})
        db.session.commit()
    except:
        return False

    sql = """SELECT id, user_id, points, answers_count, session_count, category_id, level_id, visible, created_at
        FROM games WHERE user_id=:user_id AND category_id=:category_id AND level_id=:level_id"""
    result = db.session.execute(text(sql), {"user_id":user_id, "category_id":category_id, "level_id":level_id})
    game = result.fetchone()

    if not game:
        return False
    session["game_id"] 		= game.id
    session["game_user"]	= game.user_id
    session["game_points"] 	= game.points
    session["game_answers"] 	= game.answers_count
    session["game_sessions"]	= game.session_count
    session["game_category"] 	= game.category_id
    session["game_level"] 	= game.level_id
    session["game_visible"]     = game.visible
    session["game_created"] 	= game.created_at
    return game.id
    
def question_id():
    return session.get("question_id", 0)

def question_text():
    return session.get("question_text", "")

def question_category():
    return session.get("question_category", 0)

def question_level():
    return session.get("question_level", 0)

def question_visible():
    return session.get("question_visible", False)

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

# Ask a question and handle the received answer  
def play():
    category_id = game_category()
    level_id    = game_level()
    visible     = "TRUE"
    
    # Get questions of selected category & level -> query returns list of selected questions with all info
    sql = """SELECT id, question, category_id, level_id, visible 
        FROM questions WHERE category_id=:category_id AND level_id=:level_id AND visible=:visible """
    result = db.session.execute(text(sql), {"category_id":category_id, "level_id":level_id, "visible":visible})
    questions = result.fetchall()
    # TODO: Add randomness
    question = questions[0]
    session["question_id"] = question.id
    session["question_text"] = question.question
    session["question_category"] = question.category_id
    session["question_level"] = question.level_id
    session["question_visible"] = question.visible

    # Get answer choices for the question -> query returns list of answer ids    
    question_id = question.id
    sql = """SELECT answer_id 
        FROM questions_answers WHERE question_id=:question_id"""
    result = db.session.execute(text(sql), {"question_id":question_id})
    answer_ids = result.fetchall()
    # TODO: Add randomness
    answer_1 = get_answer(answer_ids[0][0])
    answer_2 = get_answer(answer_ids[1][0])
    answer_3 = get_answer(answer_ids[2][0])

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
