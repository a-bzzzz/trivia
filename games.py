from random import shuffle
from flask import session
from sqlalchemy.sql import text
from db import db
import questions_answers

"""
Handle games
"""

game_id         = 0
game_category   = 0
game_level      = 0
sessions        = 0
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

# Get game id, points, answer amount and session amount
# of all games of one player by user id -> returns a list
def get_usergames(user_id):
    sql 	    = """SELECT id, points, answers_count, session_count
                    FROM games WHERE user_id=:user_id"""
    result 	    = db.session.execute(text(sql), {"user_id":user_id})
    usergames   = result.fetchall()
    return usergames

# Get game details by game id
def get_game(id):
    global game_id, game_category, game_level, sessions, answers, points
    visible = "TRUE"

    sql 	= """SELECT id, user_id, points, answers_count, session_count,
                    category_id, level_id, visible, created_at
                    FROM games WHERE id=:id AND visible=:visible"""
    result 	= db.session.execute(text(sql), {"id":id, "visible":visible})
    game 	= result.fetchone()

    session["game_id"] 	    = game.id
    session["game_user"]    = game.user_id
    session["game_points"]  = game.points
    session["game_answers"] = game.answers_count
    session["game_sessions"]= game.session_count
    session["game_category"]= game.category_id
    session["game_level"]   = game.level_id
    session["game_visible"] = game.visible
    session["game_created"] = game.created_at

    game_id         = game.id
    game_category   = game.category_id
    game_level      = game.level_id
    sessions        = game.session_count
    answers         = game.answers_count
    points          = game.points

    # Get the right question set (of chosen category and level) to the game
    questions = questions_answers.get_questions(game_category, game_level)

    if len(questions) < 1:
        return False

    sessions += 1
    return game.id, list(questions)

# Setup the game info to database and game session variables
def set_game_attr(user_id, category_id, level_id):
    global sessions, answers, points, game_id

    try:
        sql = """INSERT INTO games (user_id, category_id, level_id)
                VALUES (:user_id, :category_id, :level_id)
                RETURNING id, user_id, points, answers_count, session_count,
                category_id, level_id, visible, created_at"""
        result = db.session.execute(text(sql),
                {"user_id":user_id, "category_id":category_id, "level_id":level_id})
        game = result.fetchone()
        db.session.commit()

        session["game_id"] 		= game.id
        session["game_user"] 		= game.user_id
        session["game_points"] 		= game.points
        session["game_answers"] 	= game.answers_count
        session["game_sessions"]	= game.session_count
        session["game_category"] 	= game.category_id
        session["game_level"] 		= game.level_id
        session["game_visible"] 	= game.visible
        session["game_created"] 	= game.created_at

        game_id     = game.id
        sessions    = game.session_count
        answers     = game.answers_count
        points      = game.points
        return game.id
    except Exception:
        return 0

# Set session counters to default values
def clear_stats():
    global game_id, game_category, game_level, sessions, answers, points
    game_id         = 0
    game_category   = 0
    game_level      = 0
    sessions        = 0
    answers         = 0
    points          = 0
    questions_answers.clear_questionlist()
    questions_answers.clear_question_id()

# Creates new game with user id, category id and level id
# -> returns game id (by calling first "get_game_id" function)
def create_game(user, category, level):
    global game_level, sessions
    clear_stats()
    game_level = level

    # Get the right question set (of chosen category and level) to the game
    questions = questions_answers.get_questions(category, level)

    if len(questions) < 1:
        return False

    gid = set_game_attr(user, category, level)
    sessions += 1
    return gid, list(questions)

# Ask a question and handle the received answer
def play():
    global game_id
    q_details       = questions_answers.get_new_question(game_id)
    if not q_details:
        return False
    qid             = q_details[0]
    question_amount = q_details[1]
    if not qid:
        return False
    session["question_id"] = qid
    questions_answers.get_answers(qid)
    return question_amount

# Gather game statistics
def continue_game(right):
    global game_level, answers, points
    answers += 1
    # Add answer count and points, if right answer
    if right:
        points += int(game_level)

    session["game_points"]  = points
    session["game_answers"] = answers

def set_game_stats():
    global sessions, answers, points, game_id
    session_count = sessions
    answers_count = answers
    id = game_id

    try:
        sql = """UPDATE games SET points=:points,
                answers_count=:answers_count, session_count=:session_count
                WHERE games.id=:id RETURNING games.id"""
        result = db.session.execute(text(sql), {"id":id, "points":points,
                "answers_count":answers_count, "session_count":session_count})
        returned_id = result.fetchone()[0]
        db.session.commit()

        return returned_id
    except Exception:
        return 0

def game_order(game: tuple):
    return game[0]

def list_games(user_games):
    games = [g for g in user_games]
    return sorted(games, key=game_order)

# Get the created games of the player, if any, by user id
def get_user_games(user_id):
    visible = "TRUE"

    sql = """SELECT id, points, category_id, level_id
        FROM games WHERE user_id=:user_id AND visible=:visible"""
    result = db.session.execute(text(sql), {"user_id":user_id, "visible":visible})
    user_games = result.fetchall()

    if len(user_games) < 1:
        return False
    return list_games(user_games)

# Game removal: Set game visible to False, not actual db deletion
def remove_game(id):
    visible = "FALSE"
    try:
        sql = """UPDATE games SET visible=:visible WHERE games.id=:id"""
        db.session.execute(text(sql), {"id":id, "visible":visible})
        db.session.commit()
        return True
    except Exception:
        return False

# Get the best games of a player, if any, by user id, max 25 games
def get_user_best_games(user_id, rows):
    visible = "TRUE"

    sql = """SELECT ROW_NUMBER() OVER (ORDER BY points DESC, level_id DESC, session_count)
        as row_id, id, category_id, level_id, session_count, answers_count, points
        FROM games WHERE user_id=:user_id AND visible=:visible AND points>0
        ORDER BY points DESC, level_id DESC, session_count LIMIT :rows"""
    result = db.session.execute(text(sql), {"user_id":user_id, "visible":visible, "rows":rows})
    user_best_games = result.fetchall()

    if len(user_best_games) < 1:
        return False
    return user_best_games

# Get the best games of all players, if any, max 25 games
def get_best_games(rows):
    visible = "TRUE"

    sql = """SELECT ROW_NUMBER() OVER (ORDER BY G.points DESC, G.level_id DESC, G.session_count)
        as row_id, U.username, G.id, G.category_id, G.level_id, G.session_count,
        G.answers_count, G.points
        FROM games as G, users as U WHERE G.user_id=U.id AND G.visible='True' AND G.points>0
        ORDER BY G.points DESC, G.level_id DESC, G.session_count , G.answers_count LIMIT :rows"""
    result = db.session.execute(text(sql), {"visible":visible, "rows":rows})
    best_games = result.fetchall()

    if len(best_games) < 1:
        return None
    return best_games

# Get the ranking of a player's best game (if any)
def get_user_rank(user_name):
    best_list = get_best_games(500)
    for game in best_list:
        if game[1] == user_name:
            return game[0]
    return 0
