from flask import Flask, render_template

from . import db

def create_app():
    app = Flask("proj")
    app.config.from_mapping(
        DATABASE="todo"
    )

    from . import todo
    app.register_blueprint(todo.bp)

    from . import db 
    db.init_app(app) 

    return app