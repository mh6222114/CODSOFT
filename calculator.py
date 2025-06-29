import tkinter as tk

def click(event):
    current = display.get()
    new = current + str(event.widget["text"])
    display.set(new)

def clear():
    display.set("")

def calculate():
    try:
        result = eval(display.get())
        display.set(result)
    except:
        display.set("Error")

root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x400")

display = tk.StringVar()
entry = tk.Entry(root, textvar=display, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(fill="both", expand=True)
    for btn in row:
        b = tk.Button(row_frame, text=btn, font="Arial 18", height=2, width=5)
        b.pack(side="left", expand=True, fill="both")
        if btn == "C":
            b.config(command=clear)
        elif btn == "=":
            b.config(command=calculate)
        else:
            b.bind("<Button-1>", click)

root.mainloop()