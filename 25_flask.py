# flask 쓰기전 터미널 명령어
# pip install virtualenv
# virtualenv venv
# venv\scripts\activate
# pip install Flask

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

"""
# @app.route("/hello/<name>")
# def hello_world(name):
#     return "Hello %s!" % name
"""

"""
# @app.route("/flask")
# def hello_flask():
#     return "Hello Flask"


# @app.route("/python")
# def hello_python():
#     return "Hello python"
"""

"""
@app.route("/admin")
def hello_admin():
    return "Hello Admin"


@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s as Guest" % guest


@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))
"""

"""
@app.route("/success/<name>")
def success(name):
    return "welcome %s" % name


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name=user))
"""

"""
@app.route("/hello/<user>")
def hello_name(user):
    return render_template("hello.html", name=user)
"""

"""
@app.route("/")
def student():
    return render_template("student.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)
"""


@app.route("/upload")
def upload_file():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def uploader_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"


if __name__ == "__main__":
    app.run(debug=True)
