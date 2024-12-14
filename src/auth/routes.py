from flask import Blueprint, redirect, render_template, request, session

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/", methods=["GET"])
def auth_login_form_handler():
    return render_template("/auth/login_form.html")


@auth_bp.route("/", methods=["POST"])
def auth_session_handler():
    login = request.form.get("login")
    password = request.form.get("password")
    if login == "my-login" and password == "my-password":
        session["user_id"] = 1
        session["role"] = "admin"
        session.permanent = True
        return redirect("/")
    return redirect("/auth/")


def my_sum(a, b):
    return a + b
