from flask import Flask, render_template, request, url_for
import sqlite3

def init_db():
    with sqlite3.connect('club.db') as db:
        db.execute('''CREATE TABLE IF NOT EXISTS club(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            desc TEXT)''')

def add_club(name, desc):
    init_db()
    with sqlite3.connect('club.db') as db:
        db.execute("INSERT INTO club (name, desc) VALUES (?, ?)", (name, desc))

def get_club():
    init_db()
    with sqlite3.connect('club.db') as db:
        return db.execute("SELECT * FROM club").fetchall()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if 'Login' in request.form:
            return url_for('login')
        else:
            name = request.form['name']
            desc = request.form['desc']
            add_club(name, desc)
    return render_template("index.html", clubs=get_club())

@app.route('/login')
def login():
    return render_template("login.html")
