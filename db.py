import sqlite3

from flask import current_app, g


def get_db():
    if 'db' not in g: 
        dbname = current_app.config['DATABASE'] 
        g.db = sqlite3.connect(dbname)
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()