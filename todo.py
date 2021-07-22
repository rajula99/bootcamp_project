import datetime
from flask import Blueprint
from flask import render_template


bp = Blueprint("todo", "todo", url_prefix="")

today = datetime.date.today()

@bp.route("/")
def home():
    return render_template('base.html')