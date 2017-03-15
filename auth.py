from flask import Blueprint, render_template, request, redirect

from main import db_session
from user import User

auth = Blueprint("auth", __name__, template_folder="templates")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    print("signint up")
    if request.method == "POST":
        user = User(request.form["username"], request.form["password"])
        db_session.add(user)
        db_session.commit()
        return redirect('/')
    else:
        return render_template("signup.html")

@auth.route("/login")
def login():
    return "This will be the login page"
