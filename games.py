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
