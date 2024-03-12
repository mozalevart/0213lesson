from flask import Flask, render_template
from datetime import datetime
from random import random, randint

app = Flask(__name__)

@app.route("/")
def index():
    names=["Петя","Валера","Маша","Валера","Света","Коля","Никита","Вика","Артур","Валера","Дима"]
    return render_template("index.html",name=names[randint(0, len(names)-1)], now =datetime.now()), 200
@app.route("/new")
def new():
    names=["Петя","Витя","Маша","Гриша","Света","Коля","Никита","Вика","Артур","Валера","Дима"]
    return render_template("new.html",name=names[randint(0, len(names)-1)], now =datetime.now()), 200



