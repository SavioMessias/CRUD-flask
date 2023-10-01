from flask import render_template, url_for, redirect, request
from app import db,app
from models import Login

@app.route("/")
def index():
    return render_template("index.html")



#(C) CREATE:
@app.route("/new_user", methods=["POST"])
def register():
    nome = request.form["name"]
    email = request.form["email"]
    passwd = request.form["passwd"]
    
    new_user = Login(username=nome, email=email, password=passwd) # type: ignore

    teste = Login.query.where(Login.email == email).one_or_none()
    if teste is not None:
        return redirect(url_for("index"))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("index"))


#(R) READ:
@app.route("/all_users", methods=["GET"])
def view_users():
    all_users  = Login.query.all()
    return render_template("user_list.html", todos = all_users)


#(U) UPDATE:
@app.route("/updt_user", methods=["GET"])
def render_edit():
    id = request.args.get("id")
    user = Login.query.filter_by(id = id).first()
    return render_template("updt_user.html", user = user)


@app.route("/updt_user", methods=["POST"])
def update_user():
    id = request.args.get("id")
    new_name = request.form["new_name"]
    new_password = request.form["new_password"]
    Login.query.filter(Login.id == id).update({"password": new_password, "username": new_name})
    db.session.commit()
    return 'ok'


#(D) DELETE:
@app.route("/delete_user/<id>", methods=["GET","DELETE"])
def delete_user(id):
    Login.query.where(Login.id == id).delete()
    db.session.commit()
    return 'Usuario deletado com Sucesso: <a href="/">VOLTAR</a>'

