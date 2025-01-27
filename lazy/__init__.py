from sys import argv
from tkinter import *
from tkinter import ttk

from lazy import main


def play():
    button.config(state=DISABLED)
    ty.key_pressed = 'play'


def pause():
    button.config(state=NORMAL)
    ty.key_pressed = 'pause'


def stop():
    ty.key_pressed = 'stop'


def start_app():
    start_button.config(state=DISABLED)
    ty.start()
    play()


if __name__ == '__main__':
    root = Tk()
    ty = main.NoTypo('C:/Users/hilal/IdeaProjectsStudents/Python_Tutorial/ayan_class_12/clock.py')
    root.geometry("450x200")
    root.title("NoTypo")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    start_button = ttk.Button(frm, text="Start", command=start_app)
    button = ttk.Button(frm, text="Play", command=play)
    button.grid(column=1, row=0)
    start_button.grid(column=0, row=0)
    ttk.Button(frm, text="Pause", command=pause).grid(column=2, row=0)
    ttk.Button(frm, text="Stop", command=stop).grid(column=3, row=0)
    root.mainloop()
