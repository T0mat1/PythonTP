# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
from tkinter.font import Font


class Calculatrice:

    def __init__(self):
        # ============== Constants ==============
        DISPLAY_HEIGHT = 4
        KEYS_HEIGHT = 1
        WHITE = "#FFFFFF"
        BLACK = "#000000"
        # ============== Set the window ==============
        self.window = Tk()
        self.window.title("Calculatrice")
        self.window.wm_resizable(False, False)
        self.window.geometry('300x450+400+400')
        # ============== Set the font ==============
        self.font = Font(self.window, ("Arial", 20))
        # ============== Set the display ==============
        self.display = Frame(self.window, bd=0, relief="solid")
        self.display.pack()
        self.display_label = Label(self.display, text="", width=str(60), height=str(DISPLAY_HEIGHT), foreground=BLACK, background=WHITE).pack()
        # ============== Set the keys ==============
        self.rows = []
        for i in range(5):
            self.rows.append(Frame(self.window, bd=0))
        self.rows[0].pack()
        for col in range(3):
            for line in range(3):
                Button(self.rows[0], width=str(4), height=str(1), text=str(3 * line + col + 1), borderwidth=1, font=self.font).grid(row=2-line, column=col)
        Button(self.rows[0], width=str(4), height=str(1), text="%", font=self.font).grid(row=0, column=3)
        Button(self.rows[0], width=str(4), height=str(1), text="x", font=self.font).grid(row=1, column=3)
        Button(self.rows[0], width=str(4), height=str(1), text="-", font=self.font).grid(row=2, column=3)
        Button(self.rows[0], width=str(4), height=str(1), text="+", font=self.font).grid(row=3, column=3)
        Button(self.rows[0], width=str(4), height=str(1), text="0", font=self.font, borderwidth=1).grid(row=3, column=1)
        Button(self.rows[0], width=str(4), height=str(1), text="C", font=self.font).grid(row=4, column=0)
        Button(self.rows[0], width=str(4), height=str(1), text="AC", font=self.font).grid(row=4, column=1)
        Button(self.rows[0], width=str(4), height=str(1), text="=", font=self.font).grid(row=4, column=3)
        # ============== START THE APPLICATION ==============
        self.window.mainloop()

    def update_display(self, text):
        return

    def compute(self):
        return


if __name__ == "__main__":
    Calculatrice()
