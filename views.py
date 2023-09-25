from flask import render_template, url_for, redirect
from app import db, app
from models import User

@app.route("/")
def index():
    return("Hello World!")