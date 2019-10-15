# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
from tkinter.font import Font


class Calculatrice:

    def __init__(self):
        # ============== Constants ==============
        DISPLAY_HEIGHT = 5
        KEYS_HEIGHT = 1
        KEY_BORDERWIDTH = 1
        WHITE = "#FFFFFF"
        BLACK = "#000000"
        # ============== Attributes ==============
        self.isFloat = False

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
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="7", command=lambda: self.update_display(str(7)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="8", command=lambda: self.update_display(str(8)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="9", command=lambda: self.update_display(str(9)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="4", command=lambda: self.update_display(str(4)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="5", command=lambda: self.update_display(str(5)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="6", command=lambda: self.update_display(str(6)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="1", command=lambda: self.update_display(str(1)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="2", command=lambda: self.update_display(str(2)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="3", command=lambda: self.update_display(str(3)), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[3], width=str(13), height=str(KEYS_HEIGHT), text="0", command=lambda: self.update_display("0"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="%", command=lambda: self.add_symbol("/"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="x", command=lambda: self.add_symbol("*"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="-", command=lambda: self.add_symbol("-"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text="+", command=lambda: self.add_symbol("+"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="C", command=self.erase_all, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="AC", command=self.erase_last, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text=".", command=self.add_dot, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="=", command=self.compute, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)

        # ============== START THE APPLICATION ==============
        self.window.mainloop()

    def update_display(self, text):
        if self.display_label["text"] == "0":
            self.display_label["text"] = text
        else:
            self.display_label["text"] = str(self.display_label["text"]) + text

    def compute(self):
        res = eval(self.display_label["text"])
        self.isFloat = "." in str(res)
        self.display_label["text"] = str(res)

    def erase_all(self):
        self.isFloat = False
        self.display_label.config(text="0")

    def erase_last(self):
        if len(self.display_label['text']) > 1:
            if self.display_label["text"][-1] == ".":
                self.isFloat = False
            while self.display_label["text"][-1].isdigit() or self.display_label["text"][-1] == ".":
                self.display_label.config(text=self.display_label['text'][:-1])
                if self.display_label["text"] == "":
                    self.display_label["text"] = "0"
                    break;
        else:
            self.erase_all()

    def add_symbol(self, symbol):
        if self.display_label["text"][-1].isdigit():
            self.update_display(symbol)
            self.isFloat = False

    def add_dot(self):
        if self.display_label["text"] == "0":
            self.update_display("0.")
            self.isFloat = True
            return
        if not self.isFloat:
            self.update_display(".")
            self.isFloat = True


if __name__ == "__main__":
    Calculatrice()
