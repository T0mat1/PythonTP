# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *
from tkinter.font import Font


class Calculatrice:

    def __init__(self):
        # Set the window
        self.window = Tk()
        self.window.title("Calculatrice")
        self.window.wm_resizable(False, False)
        self.window.geometry('300x450+400+400')
        self.font = Font(self.window, ("Arial", 20))
        self.screen = Frame(self.window, bd=0, relief="solid")
        self.screen.pack()
        Label(self.screen, text=" ", width=str(300//5), height=str(450//6//20), foreground="#000000", background="#FFFFFF").pack()
        self.keys = Frame(self.window, bd=0, relief="solid")
        self.keys.pack()
        for col in range(3):
            for line in range(3):
                Button(self.keys, width=str(4), height=str(1), text=str(3 * line + col + 1), borderwidth=1, font=self.font).grid(row=2-line, column=col)
        Button(self.keys, width=str(4), height=str(1), text="%", font=self.font).grid(row=0, column=3)
        Button(self.keys, width=str(4), height=str(1), text="x", font=self.font).grid(row=1, column=3)
        Button(self.keys, width=str(4), height=str(1), text="-", font=self.font).grid(row=2, column=3)
        Button(self.keys, width=str(4), height=str(1), text="+", font=self.font).grid(row=3, column=3)
        Button(self.keys, width=str(4), height=str(1), text="0", font=self.font, borderwidth=1).grid(row=3, column=1)

        Button(self.keys, width=str(4), height=str(1), text="C", font=self.font).grid(row=4, column=0)
        Button(self.keys, width=str(4), height=str(1), text="AC", font=self.font).grid(row=4, column=1)
        Button(self.keys, width=str(4), height=str(1), text="=", font=self.font).grid(row=4, column=3)
        self.window.mainloop()


if __name__ == "__main__":
    Calculatrice()
