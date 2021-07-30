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


@bp.route("/", methods=["GET", "POST",])
def home():
    conn = db.get_db()
    cursor = conn.cursor()
    if request.method == "GET":
        cal = get_calender(today)
        d = dict()
        for i in range(7):   #take tasks from the week
            day = today + datetime.timedelta(days=i)
            cursor.execute("select id,task,t_status from tasks where due_date = ?", [day])
            t = cursor.fetchall()
            d[day] = t
        #day = today + datetime.timedelta(days=3)
        #cursor.execute("select * from tasks where due_date = ?", [day])
        #d=cursor.fetchall()
        return render_template('home.html', cal = cal, d = d)
    elif request.method == "POST": 
        tmp = request.form.get("updateid")
        tmp = int(tmp)
        cursor.execute("update tasks set t_status = 'done' where id = ?", [tmp])
        conn.commit()
        return redirect(url_for("todo.home", tmp = tmp), 302)
    

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