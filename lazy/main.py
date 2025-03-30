from tkinter import filedialog
from tkinter import *
from tkinter import ttk



from lazy.auto_typing import CodeGenerator



def play():
    play_button.config(state=DISABLED)
    auto_typer.play()


def pause():
    play_button.config(state=NORMAL)
    pause_button.config(state=DISABLED)
    auto_typer.pause()


def stop():
    auto_typer.stop()
    pause_button.config(state=NORMAL)
    play_button.config(state=NORMAL)
    start_button.config(state=NORMAL)
    stop_button.config(state=NORMAL)


def start_app():
    print("start app")
    start_button.config(state=DISABLED)
    auto_typer.start_app()
    play_button.config(state=DISABLED)



def open_file():
    file_path = filedialog.askopenfilename(
        title='Select a Text File', filetypes=[('All file', '*')])
    auto_typer.set_path(file_path)
    text.delete(1.0, END)
    text.insert(END, file_path)
    pause_button.config(state=NORMAL)
    play_button.config(state=NORMAL)
    start_button.config(state=NORMAL)
    stop_button.config(state=NORMAL)
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            code_preview.delete(1.0, END)
            code_preview.insert(END, content)


if __name__ == '__main__':
    window = Tk()
    file_path_ = ''
    window.geometry("800x880")
    window.title("NoTypo")
    main_frame = ttk.Frame(window, padding=5)
    main_frame.pack()
    entry_frame = ttk.Frame(main_frame)
    entry_frame.pack()
    text = Text(entry_frame, width=40, height=1)
    code_preview = Text(main_frame, wrap='word', width=400, height=50)
    code_preview.pack()
    text.pack(side=LEFT, padx=5)
    open_button = ttk.Button(entry_frame, text='Open File', command=open_file)
    open_button.pack(side=LEFT)
    button_dock = ttk.Frame(main_frame)
    button_dock.pack(padx=5, pady=5)
    start_button = ttk.Button(button_dock, text="Start", command=start_app)
    start_button.pack(side=LEFT)
    play_button = ttk.Button(button_dock, text="Play", command=play)
    play_button.pack(side=LEFT)
    pause_button = ttk.Button(button_dock, text="Pause", command=pause)
    stop_button = ttk.Button(button_dock, text="Stop", command=stop)
    pause_button.pack(side=LEFT)
    stop_button.pack(side=LEFT)
    auto_typer=CodeGenerator()
    window.mainloop()
