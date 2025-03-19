from tkinter import filedialog
from tkinter import *
from tkinter import ttk

from lazy import main

file_path = ''



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


def open_file():
    file_path_ = filedialog.askopenfilename(
        title='Select a Text File', filetypes=[('All file', '*')])
    text.delete(1.0, END)
    text.insert(END, file_path_)
    ty.link=file_path_
    if file_path_:
        with open(file_path_, 'r') as file:
            content = file.read()
            code_preview.delete(1.0, END)
            code_preview.insert(END, content)


if __name__ == '__main__':
    window = Tk()
    window.geometry("1920x1060")
    window.title("NoTypo")
    main_frame = ttk.Frame(window, padding=5)
    main_frame.pack()
    entry_frame=ttk.Frame(main_frame)
    entry_frame.pack()
    text = Text(entry_frame, width=40, height=1)
    code_preview=Text(main_frame, wrap='word', width=400, height=50)
    #v = Scrollbar(code_preview, orient='vertical')
   # v.pack(side=RIGHT, fill='y')
    #v.config(command=code_preview.yview)
    code_preview.pack()
    text.pack(side=LEFT,padx=5)
    open_button = ttk.Button(entry_frame, text='Open File', command=open_file)
    open_button.pack(side=LEFT)
    button_dock=ttk.Frame(main_frame)
    button_dock.pack(padx=5, pady=5)
    start_button = ttk.Button(button_dock, text="Start", command=start_app)
    start_button.pack(side=LEFT)
    button = ttk.Button(button_dock, text="Play", command=play)
    button.pack(side=LEFT)
    ttk.Button(button_dock, text="Pause", command=pause).pack(side=LEFT)
    ttk.Button(button_dock, text="Stop", command=stop).pack(side=LEFT)
    ty = main.NoTypo(file_path)
    window.mainloop()
