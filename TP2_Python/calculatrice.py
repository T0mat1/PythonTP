# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
from tkinter.font import Font


class Calculatrice:

    def __init__(self):
        # ============== Constants ==============
        DISPLAY_HEIGHT = 5
        KEYS_HEIGHT = 1
        WHITE = "#FFFFFF"
        BLACK = "#000000"
        # ============== Set the window ==============
        self.window = Tk()
        self.window.title("Calculatrice")
        self.window.wm_resizable(False, False)
        self.window.geometry('300x450+500+200')
        # ============== Set the font ==============
        self.font = Font(self.window, ("Arial", 20))
        # ============== Set the display ==============
        self.display = Frame(self.window, bd=1, relief="solid")
        self.display.pack()
        self.display_label = Label(self.display, text="0", font=self.font, width=str(60), height=str(DISPLAY_HEIGHT), foreground=BLACK, background=WHITE)
        self.display_label.pack()
        # ============== Set the keys ==============
        self.rows = []
        for r in range(5):
            self.rows.append(Frame(self.window, bd=0))
            self.rows[r].pack()
            if r < 3:
                for c in range(3):
                    Button(self.rows[r], width=str(4), height=str(KEYS_HEIGHT), text=str(7-3*r+c), borderwidth=1, font=self.font).grid(row=0, column=c)
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="%", font=self.font, borderwidth=1).grid(row=0, column=3)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="x", font=self.font, borderwidth=1).grid(row=0, column=3)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="-", font=self.font, borderwidth=1).grid(row=0, column=3)
        Button(self.rows[3], width=str(13), height=str(KEYS_HEIGHT), text="0", font=self.font, borderwidth=1).grid(row=0, column=0)
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text="+", font=self.font, borderwidth=1).grid(row=0, column=1)
        Button(self.rows[4], width=str(5), height=str(KEYS_HEIGHT), text="C", command=self.erase_all(), font=self.font, borderwidth=1).grid(row=0, column=0)
        Button(self.rows[4], width=str(5), height=str(KEYS_HEIGHT), text="AC", command=self.erase_last(), font=self.font, borderwidth=1).grid(row=0, column=1)
        Label(self.rows[4], width=str(5), height=str(KEYS_HEIGHT), text="").grid(row=0, column=2)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="=", font=self.font, borderwidth=1).grid(row=0, column=3)
        # ============== START THE APPLICATION ==============
        self.window.mainloop()

    def update_display(self, text):
        if self.display_label["text"] == "0":
            self.display_label["text"] = text
        else:
            self.display_label["text"] += text

    def compute(self):
        return

    def erase_all(self):
        self.display_label.config(text="0")

    def erase_last(self):
        if len(self.display_label['text']) > 1:
            self.display_label.config(text=self.display_label['text'][:-1])
        else:
            self.erase_all()


if __name__ == "__main__":
    Calculatrice()
