import os
from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from db import db

"""
Handle users
"""

def user_id():
    return session.get("user_id", 0)

def user_name():
    return session.get("user_name", None)

def user_password():
    return session.get("user_password", None)

def user_role():
    return session.get("user_role", 0)

def user_visible():
    return session.get("user_visible", None)

def user_created():
    return session.get("user_created", None)

def is_admin():
    return user_id() == 1

def get_usernames():
    sql = """SELECT username FROM users"""
    result = db.session.execute(text(sql))
    return result.fetchall()

def check_username(username):
    return username == user_name()

def login(username, password):
    sql = """SELECT id, username, password, role_id FROM users WHERE username=:username"""
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if user.role_id in (1, 2, 3):
        if not check_password_hash(user.password, password):
            return False
    session["user_id"] 	= user.id
    session["user_name"] 	= user.username
    session["user_role"] 	= user.role_id
    session["csrf_token"] 	= os.urandom(16).hex()
    return True

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password)
            VALUES (:username, :password)"""
        db.session.execute(text(sql), {"username":username, "password":hash_value})
        db.session.commit()
    except Exception:
        return False
    return login(username, password)

def logout():
    if user_id() != 0:
        del session["user_id"]
    if user_name() is not None:
        del session["user_name"]
    if user_password() is not None:
        del session["user_password"]
    if user_role() != 0:
        del session["user_role"]
    if user_visible() is not None:
        del session["user_visible"]
    if user_created() is not None:
        del session["user_created"]

def check_password(username, password):
    sql = """SELECT id, username, password, role_id FROM users WHERE username=:username"""
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not check_password_hash(user.password, password):
        return False
    return True

def change_password(username, new_password):
    password = generate_password_hash(new_password)

    try:
        sql = """UPDATE users SET password=:password WHERE username=:username"""
        db.session.execute(text(sql), {"username":username, "password":password})
        db.session.commit()
        return True
    except Exception as error:
        return error

def add_admin():
    admin 		    = "admin"
    admin_password 	= "salasana"
    admin_role		= 1
    hash_value 		= generate_password_hash(admin_password)
    sql = """INSERT INTO users (username, password, role_id)
        	VALUES (:username, :password, :role_id)"""
    db.session.execute(text(sql), {"username":admin, "password":hash_value, "role_id":admin_role})
    db.session.commit()

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
