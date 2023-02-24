from random import shuffle
from sqlalchemy.sql import text
from flask import session
from db import db

"""
Handle questions and answers
"""

question_list   = []
question_id     = 0

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

def clear_questionlist():
    global question_list
    question_list = []

def clear_question_id():
    global question_id
    question_id = 0

def answer_right():
    return session.get("answer_right", 0)

def is_right(answer):
    return answer == answer_right()

# Get answer information
def get_answer(id):

    sql = """SELECT id, answer, correct, visible FROM answers WHERE id=:id"""
    result = db.session.execute(text(sql), {"id":id})
    answer = result.fetchone()
    return answer

# Get questions of selected category & level
# -> query returns list of selected questions with all info
def get_questions(category_id, level_id):
    global question_list
    empty_session_questions()
    question_list   = []
    visible         = "TRUE"

    if int(category_id) == 6:
        sql = """SELECT id, question, category_id, level_id, visible
                FROM questions WHERE level_id=:level_id AND visible=:visible """
        result = db.session.execute(text(sql), {"level_id":level_id, "visible":visible})
        question_list = list(result.fetchall())
    else:
        sql = """SELECT id, question, category_id, level_id, visible
                FROM questions WHERE category_id=:category_id 
                AND level_id=:level_id AND visible=:visible """
        result = db.session.execute(text(sql),
                    {"category_id":category_id, "level_id":level_id, "visible":visible})
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
    if answer_1.correct:
        right_answer = 1
    session["answer_correct_2"] = answer_2.correct
    if answer_2.correct:
        right_answer = 2
    session["answer_correct_3"] = answer_3.correct
    if answer_3.correct:
        right_answer = 3

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
    if question_visible() is True:
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
def get_new_question(game_id):
    global question_list

    # Choose first question from the list,
    # and drop the fetched question from question list, if list is not empty
    if len(question_list) < 1 or question_list is None:
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
        sql = """INSERT INTO games_questions (game_id, question_id)
                VALUES (:game_id, :question_id)"""
        db.session.execute(text(sql), {"game_id":game_id, "question_id":question_id})
        db.session.commit()
    except Exception:
        return False

    return (question.id, len(question_list))

# Insert a question to questions db table with question id, level id and question text
def add_question(category_id, level_id, question):

    try:
        sql = """INSERT INTO questions (question, category_id, level_id)
        VALUES (:question, :category_id, :level_id)
        RETURNING id"""
        result = db.session.execute(text(sql), {"id":id, "question":question,
                    "category_id":category_id, "level_id":level_id})     
        question = result.fetchone()
        db.session.commit()
        return question.id
    except Exception:
        return 0

# Insert all answer alternatives to answers db table
# 1st and 2nd with default correct value (False)
# 3rd, the RIGHT answer, with correct value True
def add_answers(answer1, answer2, answer3):

    try:
        # 1st wrong answer
        answer = answer1
        sql = """INSERT INTO answers (answer) VALUES (:answer) RETURNING id"""
        result = db.session.execute(text(sql), {"id":id, "answer":answer})
        answer_1 = result.fetchone()
        db.session.commit()
        id1 = answer_1.id
        # 2nd wrong answer
        answer = answer2
        sql = """INSERT INTO answers (answer) VALUES (:answer) RETURNING id"""
        result = db.session.execute(text(sql), {"id":id, "answer":answer})
        answer_2 = result.fetchone()
        db.session.commit()
        id2 = answer_2.id
        # The RIGHT answer
        answer = answer3
        correct = "TRUE"
        sql = """INSERT INTO answers (answer, correct) VALUES (:answer, :correct) RETURNING id"""
        result = db.session.execute(text(sql), {"id":id, "answer":answer, "correct":correct})
        answer_3 = result.fetchone()
        db.session.commit()
        id3 = answer_3.id

        return [id1, id2, id3]
    except Exception:
        return []

# Insert one question-answer pair to questions_answers db table
def insert_qa(question_id, answer_id):
    try:
        sql = """INSERT INTO questions_answers (question_id, answer_id)
                VALUES (:question_id, :answer_id)"""
        db.session.execute(text(sql), {"question_id":question_id, "answer_id":answer_id})
        db.session.commit()
        return 1
    except Exception:
        return 0

# Handle all answer alternatives for combining them with the related question
def add_qa(qid, answer_ids):
    ok = 0
    for answer_id in answer_ids:
        add = insert_qa(qid, answer_id)
        ok += add
    if ok < 3:
        return False
    return True
