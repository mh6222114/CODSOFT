from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def save_task():
    task = task_input.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task field is empty!")
    else:
        task_data.append(task)
        db_cursor.execute("INSERT INTO tasklist VALUES (?)", (task,))
        refresh_tasks()
        task_input.delete(0, END)

def refresh_tasks():
    task_display.delete(0, END)
    for item in task_data:
        task_display.insert(END, item)

def remove_task():
    try:
        selected = task_display.get(task_display.curselection())
        task_data.remove(selected)
        refresh_tasks()
        db_cursor.execute("DELETE FROM tasklist WHERE name = ?", (selected,))
    except:
        messagebox.showerror("Error", "Select a task to delete.")

def remove_all():
    if messagebox.askyesno("Delete All", "Want to delete everything?"):
        task_data.clear()
        db_cursor.execute("DELETE FROM tasklist")
        refresh_tasks()

def load_tasks():
    task_data.clear()
    for entry in db_cursor.execute("SELECT name FROM tasklist"):
        task_data.append(entry[0])

def close_app():
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("My Task Manager")
    root.geometry("660x400+550+250")
    root.configure(bg="#DFF6FF")
    root.resizable(False, False)

    db_conn = sql.connect("tasks.db")
    db_cursor = db_conn.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS tasklist (name TEXT)")

    task_data = []

    top_frame = Frame(root, bg="#B2D3C2")
    top_frame.pack(expand=True, fill="both")

    heading = Label(top_frame, text="My TO-DO App", bg="#B2D3C2", fg="#303030",
                    font=("Verdana", 16, "bold"))
    heading.place(x=20, y=20)

    task_input = Entry(top_frame, width=40, font=("Verdana", 13))
    task_input.place(x=200, y=25)

    Button(top_frame, text="Add Task", bg="#FFD966", font=("Verdana", 12),
           command=save_task).place(x=20, y=70)
    Button(top_frame, text="Remove Task", bg="#FFD966", font=("Verdana", 12),
           command=remove_task).place(x=180, y=70)
    Button(top_frame, text="Clear All", bg="#FFD966", font=("Verdana", 12),
           command=remove_all).place(x=360, y=70)
    Button(top_frame, text="Exit App", bg="#FF7373", font=("Verdana", 12),
           command=close_app).place(x=500, y=330)

    task_display = Listbox(top_frame, width=65, height=10, selectmode=SINGLE,
                           font=("Segoe UI", 11), bg="white", fg="#202020",
                           selectbackground="#D26F2B")
    task_display.place(x=20, y=130)

    load_tasks()
    refresh_tasks()
    root.mainloop()

    db_conn.commit()
    db_cursor.close()