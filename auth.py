from flask import Blueprint, render_template, request, redirect, session
from database import db_session
from user import User
from base import Base

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")

def validate_user(username, password):
    user = db_session.query(User).filter_by(username=username).first()
    if not user and username != '' and password != '':
        return True
    else:
        return False


def find_user(username, password):
    user = db_session.query(User).filter_by(username=username,
        password=password).first()
    return user

@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        if validate_user(request.form["username"], request.form["password"]):
            user = User(request.form["username"], request.form["password"])
            db_session.add(user)
            db_session.commit()
            session['user_id'] = request.form["username"]
            return redirect('/')
        else:
            error = 'You did something wrong'
    return render_template("signup.html", error=error)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if find_user(request.form["username"], request.form["password"]):
            session["user_id"] = request.form["username"]
            return redirect("/")
        else:
            error = "You did something wrong"
    return render_template("login.html", error=error)

@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    session["user_id"] = None
    return redirect("/")
