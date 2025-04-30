import sqlite3

db = sqlite3.connect("clubs.db")
cursor = db.cursor()
cursor.execute("create table if not exists club (id integer, name text, desc text)")
db.commit()

def add_club(name, desc):
    _id = cursor.execute("select max(id)+1 from club")
    _id = _id.fetchone()[0]
    cursor.execute("insert into club(id, name, desc) values(?, ?, ?)", (_id, name, desc))
    db.commit()
