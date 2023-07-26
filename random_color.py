import tkinter as tk
import random

def random_color():
    colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'D', 'C', 'E', 'F']
    final_color = '#'
    for _ in range(6):
        final_color += random.choice(colors)
    win.config(bg=final_color)
    label1.config(text=final_color)

win = tk.Tk()
win.geometry('500x500')
win.resizable(0, 0)

button1 = tk.Button(win, text='Click here to change background', font='Sylfaen 12', command=random_color)
button1.place(x=130, y=100)

label1 = tk.Label(win, font='Sylfaen 12')
label1.place(x=200, y=150)

win.mainloop()
