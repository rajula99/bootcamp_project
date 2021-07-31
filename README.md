# TODO LIST MANAGER - single user

---------------Running------------------
1) export FLASK_APP=proj
2) export FLASK_ENV=development
3) flask initdb
4) flask run
----------------------------------------


Database is empty now. Add tasks by clicking 'add tasks' button. 
You can select any date from the next week from datepicker, add multiple tasks(should be seperated by comma).

Update tasks by checking the corresponding checkbox and clicking 'update' button.

---------update only ONE TASK AT A TIME---------

updating multiple tasks doesn't work :(



-------------checking overdue tasks-------------

You can add some tasks(keep them unchecked) and change the value of 'today' to some later date in the week.

todo.py > line 11 > #+ datetime.timedelta(days=1)
uncomment and you can the change value of 'days=' too. Run again and overdue tasks would appear if there are any.


---------------------------------------------------------------------------------------------------------------
