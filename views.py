from flask import render_template, url_for, redirect, request
from app import db,app
from models import Login


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/newUser", methods=["POST"])
def register():
    nome = request.form["name"]
    email = request.form["email"]
    passwd = request.form["passwd"]
    
    newUser = Login(username=nome, email=email, password=passwd)

    teste = Login.query.where(Login.email == email).one_or_none()
    if teste is not None:
        return redirect(url_for("index"))

    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/allUsers", methods=["GET"])
def seeUsername():
    allUsers  = Login.query.all()
    return render_template("userList.html", todos = allUsers)

@app.route("/deleteUser/<id>", methods=["GET","DELETE"])
def deleteUser(id):
    print(Login.query.where(Login.id == id).one_or_none())
    Login.query.where(Login.id == id).delete()
    db.session.commit()
    return 'Usuario deletado com Sucesso: <a href="/">VOLTAR</a>'