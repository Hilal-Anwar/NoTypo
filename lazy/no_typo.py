import threading
import time

import pyautogui
import pygetwindow
import pyperclip


class NoTypo(threading.Thread):
    list_key = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    status = 'play'
    active_window =  pygetwindow.getActiveWindowTitle()
    special_list = ["[", "{", "("]
    key_pressed = 'play'
    link = ''
    thread_status = 'stop'

    def __init__(self, link):
        threading.Thread.__init__(self)
        self.link = link

    def start_typing(self):
        w = 0
        self.thread_status='play'
        time.sleep(5)
        self.active_window = pygetwindow.getActiveWindowTitle()
        file = open(self.link, 'r+')
        for da in file:
            data = da.replace("\n", "")
            k = 0
            s = ""
            for i in data:
                current = pygetwindow.getActiveWindowTitle()
                if i in self.list_key or i.lower() in self.list_key:
                    if i in self.special_list:
                        self.type_for_me(i)
                    else:
                        if i == '"':
                            if k == 2:
                                self.type_for_me(i)
                            else:
                                pyautogui.typewrite(s + i, interval=0.01)
                            k = k + 1
                        elif i != '"':
                            if i == " ":
                                s = s + i
                            else:
                                pyautogui.typewrite(s + i)
                                s = ""
                else:
                    pyperclip.copy(i)
                    with pyautogui.hold("ctrl"):
                        pyautogui.press("v")
                if self.key_pressed == 'pause' or current != self.active_window:
                    while self.key_pressed == 'pause' or current != self.active_window:
                        s = i
                        current = pygetwindow.getActiveWindowTitle()
                        if self.key_pressed == 'stop':
                            break
                elif self.key_pressed == 'stop'or self.thread_status == 'stop':
                    w = 1
                    break
            if w == 1:
                self.thread_status = 'stop'
                break
            with pyautogui.hold("ctrl"):
                pyautogui.press("e")
            pyautogui.press("enter")
            with pyautogui.hold("ctrl"):
                pyautogui.press("b")

    @staticmethod
    def type_for_me(i):
        pyautogui.typewrite(i)
        pyautogui.press("right")
        pyautogui.press("backspace")

    def run(self):
        self.start_typing()
