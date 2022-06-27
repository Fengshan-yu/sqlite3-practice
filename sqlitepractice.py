import sqlite3
import tkinter as tk


class ToDo:
    task_name = []

    def __init__(self):
        self.conn = sqlite3.connect("todo1.db")
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter priority: "))

        self.c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", (name, priority))
        self.conn.commit()

    def find_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter priority: "))

        if name == "":
            pass
        elif priority < 1:
            pass
        elif name not in ToDo.task_name:
            ToDo.task_name.append(name)
            self.c.execute("SELECT * FROM tasks")
            rows = self.c.fetchall()
            for row in rows:
                if row[1] == name:
                    print(row)
                else:
                    print(None)
        elif name in ToDo.task_name:
            pass

    def change_priority(self):
        id = int(input("Enter the id: "))
        priority = int(input("Enter the priority to be set: "))

        self.c.execute("UPDATE tasks SET priority = ? WHERE id=?", (priority, id))
        self.conn.commit()

    def delete_task(self):
        id = int(input("Enter the id: "))

        self.c.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()

    # static method
    def show_tasks():
        conn = sqlite3.connect("todo1.db")
        c = conn.cursor()
        for row in c.execute("SELECT * FROM tasks"):
            print(row)

def Click1():
    return ToDo.show_tasks()

def Click2():
    return my_task.add_task()

def Click3():
    return my_task.change_priority()

def Click4():
    return my_task.delete_task()

def Click5():
    window.destroy();

my_task=ToDo()
window = tk.Tk()
window.title("Choose your task")
button_1 = tk.Button(window, text="Show Tasks", command=Click1)
button_2 = tk.Button(window, text="Add Task", command=Click2)
button_3 = tk.Button(window, text="Change Priority", command=Click3)
button_4 = tk.Button(window, text="Delete Task", command=Click4)
button_5 = tk.Button(window, text="Exit", command=Click5)
button_1.place(x=10, y=10, width=100)
button_2.place(x=10, y=50, width=100)
button_3.place(x=10, y=90, width=100)
button_4.place(x=10, y=130, width=100)
button_5.place(x=10, y=170, width=100)
window.mainloop()