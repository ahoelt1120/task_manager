from task_manager import TaskManager
from task import Task
from tkinter import *
from tkinter import ttk
root = Tk()

task_manager = TaskManager()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=0)
root.geometry("800x800+0+0")

# Title of GUI window
label_title = Label(root, text="Task Manager", font=("Arial", 37, "bold"), fg="white")
label_title.place(x=0, y=0, width=800, height=50)

# Creating new task
task_label = Label(root, text="Create New Task", font=("Arial", 23, "bold"), fg="white")
task_label.place(x=150, y=70, width=500, height=50)

# Add task name label
task_name = Label(root, text="Task name:", font=("Arial", 13, "bold"), fg="white")
task_name.place(x=250, y=120, width=100, height=30)

# Adding text entry box for task name
input_taskname = Entry(root, width = 50)
input_taskname.place(x= 350, y = 120, width=200, height = 30)

# task due date
task_due = Label(root, text="Task Due Date:", font=("Arial", 13, "bold"), fg="white")
task_due.place(x=260, y=160, width=100, height=30)

# Date slash
date_marker = Label(root, text="/", font=("Arial", 17, "bold"), fg="white")
date_marker.place(x=395, y=160, width=40, height=30)

# Month input box
month = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
)
month.place(x= 360, y = 160, width=50, height = 30)

# Another date slash
task_due = Label(root, text="/", font=("Arial", 17, "bold"), fg="white")
task_due.place(x=455, y=160, width=40, height=30)

# Day input box
day = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
            "24", "25", "26", "27", "28", "29", "30", "31"]
)
day.place(x= 420, y = 160, width=50, height = 30)

# Year input box
year = ttk.Combobox(
    state="readonly",
    values=["2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033",
            "2034", "2035", "2036"]
)
year.place(x= 480, y = 160, width=60, height = 30)





# Task due time
task_time = Label(root, text="Task Time Due:", font=("Arial", 13, "bold"), fg="white")
task_time.place(x=260, y=200, width=100, height=30)

# Time colon label
task_due = Label(root, text=":", font=("Arial", 17, "bold"), fg="white")
task_due.place(x=395, y=200, width=40, height=30)

# Hour task is due
hour = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
)
hour.place(x= 360, y = 200, width=50, height = 30)


# Minute task due
minute = ttk.Combobox(
    state="readonly",
    values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
            "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
            "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
            "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
)
minute.place(x= 420, y = 200, width=50, height = 30)

# Task is due in am or pm
pm_am = ttk.Combobox(
    state="readonly",
    values=["AM","PM"]
)
pm_am.place(x= 470, y = 200, width=50, height = 30)


# Functionality for the button
def myClick():
    '''Checks that all blanks were filled before using the input to create a
    task object and then printing each object in the todo list'''

    if ((input_taskname.get() == "") or (year.get() == "") or (month.get() == "") or (day.get() == "")
        or (hour.get() == "") or (minute.get() == "") or (pm_am.get() == "")):
        return

    new_task = Task(input_taskname.get(), int(year.get()), int(month.get()), int(day.get()), int(hour.get()), int(minute.get()), pm_am.get())

    task_manager.add_task(new_task)
    # Updating task list
    start_y = 350
    for task in task_manager.tasks:
        new_label = Label(root, text=str(task), font=("Arial", 12, "bold"), fg="white")
        new_label.place(x= 0, y = start_y, width=800, height = 30)
        start_y += 25


# The add task button that calls myClick()
myButton = Button(root, text="Add task",command=myClick)
myButton.place(x= 375, y = 250, width=80, height = 30)

# Task list label
task_label = Label(root, text="Current Task List", font=("Arial", 23, "bold"), fg="white")
task_label.place(x=150, y=300, width=500, height=50)





root.mainloop()


