from flask import render_template, request, redirect, session
from app import app
import users
import games
import questions_answers

"""
Handle game navigation
"""

@app.route("/")
def index():
    usernames = users.get_usernames()
    if ('admin',) not in usernames:
        users.add_admin()
    return render_template("index.html", count=len(usernames), users=usernames)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            message = "Wrong username or password - Väärä tunnus tai salasana"
            return render_template("error.html", message=message)
        return redirect("/")

@app.route("/logout")
def logout():
    if request.method == "GET":
        users.logout()
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username    = request.form["username"]
        password1   = request.form["password1"]
        password2   = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords differ - Salasanat eroavat")
        if not users.register(username, password1):
            message="Registration failed - Rekisteröinti ei onnistunut"
            return render_template("error.html", message=message)
        return redirect("/")

@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if request.method == "GET":
        return render_template("change_password.html")

    if request.method == "POST":
        username = request.form["username"]
        old_password = request.form["password1"]
        new_password = request.form["password2"]
        users.check_csrf()
        if not users.is_admin():
            if old_password == new_password:
                message="Give different password! - Anna eri salasana!"
                return render_template("error.html", message=message)
        password_match = users.check_password(username, old_password)
        if users.is_admin():
            password_match = True
        user_match = username == users.user_name()
        if not (password_match and user_match):
            if not users.is_admin():
                message="Unauthorized password change - Ei oikeutta vaihtaa tätä salasanaa"
                return render_template("error.html", message=message)
        change_ok = users.change_password(username, old_password, new_password)
        if not change_ok:
            message="Password change failed - Salasanan vaihto ei onnistunut"
            return render_template("error.html", message=message)
        message = f"Password changed for user {username} - Salasana vaihdettu käyttäjälle {username}"
        return render_template("change_password.html", message=message)

@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "GET":
        message=""
        return render_template("menu.html", user_id=users.user_id(), user_name=users.user_name(), message=message)

    if request.method == "POST":
        user_id 		= users.user_id()
        category 		= int(request.form["cat"])
        level 			= int(request.form["lev"])
        users.check_csrf()

        session["category_id"]	= category
        session["level_id"]	= level

        game_details = games.create_game(user_id, category, level)
        if not game_details:
            message="No questions: Choose other category/level! - Ei kysymyksiä: Valitse toinen kategoria/taso!"
            return render_template("error.html", message=message)

        game_id         	= game_details[0]
        question_list   	= game_details[1]

        session["game_sessions"] = games.game_sessions()

        if game_id == 0:
            no_game_message = f"Game creation failed - Pelin luonti ei onnistunut - Game id: {game_id}"
            return render_template("error.html", message=no_game_message)

        question_amount = games.play()
        game_on = True

        quit_message= ""
        if question_amount < 1:
            game_on         = False
            quit_message    = "No more questions, choose new game category/level - Ei lisää kysymyksiä, valitse uusi kategoria/taso"
            return render_template("check.html", question_amount=question_amount, game_on=game_on, q_message=quit_message)
        return render_template("game.html", questions=question_list)

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        games.play()
        return render_template("game.html")

    if request.method == "POST":
        answered 	= int(request.form["answer"])
        users.check_csrf()
        result_message	= ""
        right 		= questions_answers.is_right(answered)
        if right:
            result_message = "Right answer! - Oikea vastaus!"
        else:
            result_message = "Wrong answer! - Väärä vastaus!"

        games.continue_game(right)
        gid 	= games.set_game_stats()
        if gid == 0:
            message	= "Data storage to database failed - Pelitiedot eivät tallentuneet tietokantaan"
        else:
            message	= f"Game no {gid} details stored to database - Pelin nro {gid} tiedot tallennettu tietokantaan"
        question_amount = questions_answers.question_amount()
        quit_message    = ""
        if question_amount < 1:
            quit_message = "No more questions, choose new game category/level- Ei lisää kysymyksiä, valitse uusi pelikategoria/-taso"
        return render_template("check.html", result_message=result_message, message=message, question_amount=question_amount, q_message=quit_message)

@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "GET":
        return render_template("check.html")

    if request.method == "POST":
        questions_answers.empty_session_questions()
        questions_answers.empty_session_answers()
        return redirect("/")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        user_id = users.user_id()
        gamelist = games.get_user_games(user_id)
        if not gamelist:
            message="No prior games: Create new game! - Ei aiempia pelejä: Luo uusi peli!"
            return render_template("error.html", message=message)
        return render_template("search.html", gamelist=gamelist)

    if request.method == "POST":
        game_id                     = int(request.form["gid"])
        users.check_csrf()
        game_details                = games.get_game(game_id)

        if not game_details:
            message="No questions: Choose other category/level! - Ei kysymyksiä: Valitse toinen kategoria/taso!"
            return render_template("error.html", message=message)

        game_id                     = game_details[0]
        question_list               = game_details[1]

        session["game_sessions"]    = games.game_sessions()

        if game_id == 0:
            no_game_message = f"Game search failed - Pelin haku ei onnistunut - Game id: {game_id}"
            return render_template("error.html", message=no_game_message)

        question_amount             = games.play()
        game_on                     = True

        quit_message= ""
        if question_amount < 1:
            game_on = False
            quit_message = "No more questions, choose new game category/level- Ei lisää kysymyksiä, valitse uusi pelikategoria/-taso"
            return render_template("check.html", question_amount=question_amount, game_on=game_on, q_message=quit_message)
        return render_template("game.html", questions=question_list)

@app.route("/search_remove", methods=["GET", "POST"])
def search_remove():
    if request.method == "GET":
        user_id             = users.user_id()
        gamelist            = games.get_user_games(user_id)
        if not gamelist:
            message="No prior games: Create new game! - Ei aiempia pelejä: Luo uusi peli!"
            return render_template("error.html", message=message)
        return render_template("search_remove.html", gamelist=gamelist)

    if request.method == "POST":
        game_id             = int(request.form["gid"])
        users.check_csrf()
        game_details        = games.get_game(game_id)
        game_id             = game_details[0]

        if game_id == 0:
            no_game_message = f"Game search failed - Pelin haku ei onnistunut - Game id: {game_id}"
            return render_template("error.html", message=no_game_message)
        gid                 = game_id
        message = f"Trying to remove game no {gid} - Poistamassa peliä nro {gid}"
        return render_template("delete.html", gid=game_id, message=message)

@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        gid     = int(request.form["gid"])
        users.check_csrf()
        deleted = games.remove_game(gid)
        if not deleted:
            message="Deletion failed - Poistaminen epäonnistui"
            return render_template("error.html", message=message)
        message = f"Game no {gid} deleted - Peli nro {gid} poistettu"
        return render_template("delete.html", gid=gid, message=message)

@app.route("/add_questions_answers", methods=["GET", "POST"])
def add_questions_answers():

    if request.method == "GET":
        return render_template("add_questions_answers.html")

    if request.method == "POST":

        category                    = int(request.form["cat"])
        level                       = int(request.form["lev"])
        users.check_csrf()

        session["category_id"]      = category
        session["level_id"]         = level

        question                    = request.form["question"]
        answer1                     = request.form["answer1"]
        answer2                     = request.form["answer2"]
        answer3                     = request.form["answer3"] # the RIGHT answer

        qid = questions_answers.add_question(category, level, question)
        if qid == 0:
            message="Adding question failed - Kysymyksen lisäys epäonnistui"
            return render_template("error.html", message=message)
        answer_ids = questions_answers.add_answers(answer1, answer2, answer3)
        if len(answer_ids) < 1:
            message="Adding answers failed - Vastausten lisäys epäonnistui"
            return render_template("error.html", message=message)
        add_ok = questions_answers.add_qa(qid, answer_ids)
        if not add_ok:
            message = "Adding question-answers failed - Kysymys-vastaus-lisäys epäonnistui"
            return render_template("error.html", message=message)
        add_message = f"ADDED: question {qid}, answers {answer_ids[0]}, {answer_ids[1]}, {answer_ids[2]}"
        return render_template("add_questions_answers.html", message=add_message)
