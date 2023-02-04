from app import app
from flask import render_template, request, redirect
import users, games

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 3 or len(username) > 20:
            return render_template("error.html", message="Username contains 3-20 characters - Tunnuksessa tulee olla 3-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords differ - Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Enter password - Syötä salasana")
        if not users.register(username, password1):
            return render_template("error.html", message="Registration failed - Rekisteröinti ei onnistunut")
        return redirect("/")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "GET":
        return render_template("menu.html", user_id=users.user_id(), user_name=users.user_name())

    if request.method == "POST":
        user_id = users.user_id()
        category = request.form["cat"]
        level = request.form["lev"]

        if category not in ("1", "2", "3", "4", "5", "6"):
            return render_template("error.html", message="Choose category - Valitse kategoria")
        if level not in ("1", "2", "3"):
            return render_template("error.html", message="Choose level - Valitse taso")

        game_id = games.create_game(user_id, category, level)
        if not game_id or game_id == 0:
            return render_template("error.html", message="Game creation failed - Pelin luonti ei onnistunut")

        right_answer = games.play()
        return render_template("game.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("game.html")

    if request.method == "POST":
        answered = int(request.form["answer"])
        result_message = ""
        if games.is_right(answered):
            result_message = "Right answer! - Oikea vastaus!"
        else:
            result_message = "Wrong answer! - Väärä vastaus!"

        return render_template("check.html", message=result_message)
