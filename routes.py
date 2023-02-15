from app import app
from flask import render_template, request, redirect, session
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
            return render_template("error.html", message="Wrong username or password - Väärä tunnus tai salasana")
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
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords differ - Salasanat eroavat")
        if not users.register(username, password1):
            return render_template("error.html", message="Registration failed - Rekisteröinti ei onnistunut")
        return redirect("/")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "GET":
        message=""
        return render_template("menu.html", user_id=users.user_id(), user_name=users.user_name(), message=message)
         
    if request.method == "POST":
        user_id = users.user_id()
        category = int(request.form["cat"])
        level = int(request.form["lev"])

        session["category_id"]  = category
        session["level_id"]     = level

        game_details = games.create_game(user_id, category, level)
        if not game_details:
            return render_template("error.html", message="No questions: Choose other category/level! - Ei kysymyksiä: Valitse toinen kategoria/taso!")            

        game_id         = game_details[0]
        question_list   = game_details[1]
        
        session["game_sessions"]    = games.game_sessions()
        
        if game_id == 0:
            no_game_message = f"Game creation failed - Pelin luonti ei onnistunut - Game id: {game_id}"
            return render_template("error.html", message=no_game_message)

        question_amount = games.play()
        game_on = True

        quit_message= ""
        if question_amount < 1:
            game_on = False
            quit_message = "No more questions, choose new game category/level- Ei lisää kysymyksiä, valitse uusi pelikategoria/-taso"
            return render_template("check.html", message=result_message, question_amount=question_amount, game_on=game_on, q_message=quit_message)
        return render_template("game.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        games.play()
        return render_template("game.html")

    if request.method == "POST":
        answered = int(request.form["answer"])
        result_message = ""
        right = games.is_right(answered)
        if right:
            result_message = "Right answer! - Oikea vastaus!"
        else:
            result_message = "Wrong answer! - Väärä vastaus!"
            
        game_on = games.continue_game(right)
        gid = games.set_game_stats()
        if gid == 0:
            message="Unsuccessful data storage to database - Pelitiedot eivät tallentuneet tietokantaan"
        else:
            message=f"Game no {gid} details stored to database - Pelin nro {gid} tiedot tallennettu tietokantaan"      
    
        question_amount = games.question_amount()
        quit_message= ""
        if not game_on:
            quit_message = "No more questions, choose new game category/level- Ei lisää kysymyksiä, valitse uusi pelikategoria/-taso"
            return render_template("check.html", message=result_message, question_amount=question_amount, game_on=game_on, q_message=quit_message)
            

@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "GET":
        return render_template("check.html")
            
    if request.method == "POST":
        games.empty_session_questions()
        games.empty_session_answers()
        return redirect("/")
        
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        user_id = users.user_id()
        gamelist = games.get_user_games(user_id)
        if not gamelist:
            return render_template("error.html", message="No prior games: Create new game! - Ei aiempia pelejä: Luo uusi peli!")
        else:
            return render_template("search.html", gamelist=gamelist)
            
    if request.method == "POST":
        game_id = int(request.form["gid"])
        game_details = games.get_game(game_id)

        # game_details = games.create_game(user_id, category, level)
        if not game_details:
            return render_template("error.html", message="No questions: Choose other category/level! - Ei kysymyksiä: Valitse toinen kategoria/taso!")            

        game_id         = game_details[0]
        question_list   = game_details[1]

        session["game_sessions"]    = games.game_sessions() 
        
        if game_id == 0:
            no_game_message = f"Game search failed - Pelin haku ei onnistunut - Game id: {game_id}"
            return render_template("error.html", message=no_game_message)

        question_amount = games.play()
        game_on = True

        quit_message= ""
        if question_amount < 1:
            game_on = False
            quit_message = "No more questions, choose new game category/level- Ei lisää kysymyksiä, valitse uusi pelikategoria/-taso"
            return render_template("check.html", question_amount=question_amount, game_on=game_on, q_message=quit_message)
        return render_template("game.html", questions=question_list)

