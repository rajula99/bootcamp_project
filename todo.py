import datetime
import calendar
from flask import Blueprint
from flask import render_template, g

from . import db


bp = Blueprint("todo", "todo", url_prefix="")

today = datetime.date.today()

def get_calender(tdy):
    today = datetime.date.today()
    mnth = int(today.strftime('%m'))
    yr = int(today.strftime('%y'))
    return calendar.month(yr, mnth)


@bp.route("/")
def home():
    conn = db.get_db()
    cursor = conn.cursor()
    cal = get_calender(today)
    '''d = dict()
    for i in range(7):
        cursor.execute("select * from schedule where due_date = today - datetime.timedelta(days={})".format(i))
        todo = cursor.fetchall()
        due = todo[0](2)
        d[due] = todo
        '''
    return render_template('home.html', cal = cal)