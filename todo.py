import datetime
import calendar
from flask import Blueprint
from flask import render_template, request, redirect, url_for, g

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
    cursor.execute("select * from tasks")
    res = cursor.fetchall()
    return render_template('home.html', cal = cal, res = res)

@bp.route("/add", methods=["GET", "POST",])
def addtask():
    conn = db.get_db()
    cursor = conn.cursor()

    if request.method == "GET":
        to_date = today + datetime.timedelta(days=7)
        return render_template('addpage.html', today = today, to_date = to_date)
    elif request.method == "POST":
        due = request.form.get("due-date")
        tasks = request.form.get("tasks")
        t_lst = tasks.split(',')
        for i in t_lst:
            cursor.execute("insert into tasks (task, due_date, t_status) values (?, ?, 'active')", [i, due])
        conn.commit()
        return redirect(url_for("todo.home"))