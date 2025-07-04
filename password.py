from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random

def generate_password():
    try:
        length = pwd_length.get()
        characters = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(characters)
        password.set("".join(characters[:length]))
    except:
        messagebox.showerror("Oops!", "Kuch galti ho gayi! Try again.")

def on_hover(event):
    generate_button.config(bg="#3B3B3B", fg="white")

def on_leave(event):
    generate_button.config(bg="#FFC300", fg="black")

# GUI Setup
root = Tk()
root.title("SecurePass - Generator")
root.geometry("500x350")
root.config(bg="#F7F1E5")
root.resizable(False, False)

# Title Label
Label(root, text="💡 Secure Password Generator", font=("Verdana", 16, "bold"),
      bg="#F7F1E5", fg="#2C3E50").pack(pady=20)

# Password length
Label(root, text="Password length:", font=("Calibri", 12), bg="#F7F1E5", fg="green").place(x=40, y=90)
pwd_length = IntVar()
length_chooser = Combobox(root, textvariable=pwd_length, state="readonly", font=("Calibri", 11))
length_chooser['values'] = list(range(4, 31))
length_chooser.current(8)
length_chooser.place(x=180, y=90)

# Generate Button
generate_button = Button(root, text="Create Password", font=("Helvetica", 12, "bold"),
                         bg="#FFC300", fg="black", command=generate_password, cursor="hand2")
generate_button.place(x=170, y=140)
generate_button.bind("<Enter>", on_hover)
generate_button.bind("<Leave>", on_leave)

# Result display
Label(root, text="Your Password:", font=("Calibri", 12), bg="#F7F1E5", fg="green").place(x=40, y=200)
password = StringVar()
Entry(root, textvariable=password, font=("Consolas", 14), state="readonly", width=25,
      fg="#1A5276", bd=2).place(x=170, y=200)

root.mainloop()