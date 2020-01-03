# -*- coding: utf-8 -*-
# TP2 Python - Thomas ROSSI & Emeric PAIN
from functools import partial
from tkinter import *
from tkinter.font import Font

# ============== Set the "about" window ==============
def display_about_popup():
    window = Toplevel()
    window.wm_title("À propos")
    window.geometry("300x50+500+300")
    window.wm_resizable(False, False)
    Label(window, text="Calculatrice [Version 1.2]").pack()
    Label(window, text="Auteurs : Emeric Pain & Thomas Rossi").pack()
    window.mainloop()


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
        self.inErrorState = False

        # ============== Set the window ==============
        self.window = Tk()
        self.window.title("Calculatrice")
        self.window.wm_resizable(False, False)
        self.window.geometry('300x450+500+200')

        # ============== Set the menubar ==============
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.menu_option = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Options", menu=self.menu_option)
        self.menu_option.add_command(label="Scientifique")
        self.menubar.add_command(label="Quitter", command=self.window.quit)
        self.menubar.add_command(label="?", command=display_about_popup)

        # ============== Set the font ==============
        self.font = Font(self.window, ("Arial", 20))

        # ============== Set the display ==============
        self.display = Frame(self.window, bd=1, relief="solid")
        self.display.pack()
        self.display_label = Label(self.display, text="0", anchor="c", font=self.font, width=str(60), height=str(DISPLAY_HEIGHT), foreground=BLACK, background=WHITE)
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
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text="(", command=lambda: self.update_display("("), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text=")", command=lambda: self.update_display(")"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text="0", command=lambda: self.update_display("0"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[0], width=str(4), height=str(KEYS_HEIGHT), text="÷", command=lambda: self.add_symbol("/"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[1], width=str(4), height=str(KEYS_HEIGHT), text="×", command=lambda: self.add_symbol("*"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[2], width=str(4), height=str(KEYS_HEIGHT), text="-", command=lambda: self.add_symbol("-"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[3], width=str(4), height=str(KEYS_HEIGHT), text="+", command=lambda: self.add_symbol("+"), font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="C", command=self.erase_all, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=0)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="AC", command=self.erase_last, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=1)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text=".", command=self.add_dot, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=2)
        Button(self.rows[4], width=str(4), height=str(KEYS_HEIGHT), text="=", command=self.compute, font=self.font, borderwidth=KEY_BORDERWIDTH).grid(row=0, column=3)

        # ============== START THE APPLICATION ==============
        self.window.mainloop()

    def update_display(self, text):
        if not self.inErrorState :
            if self.display_label["text"] == "0":
                if text == ")":
                    self.display_label["text"] = "0"
                else:
                    self.display_label["text"] = text
            else:
                self.display_label["text"] = str(self.display_label["text"]) + text

    def compute(self):
        if not self.inErrorState:
            try:
                res = eval(self.display_label["text"])
                self.isFloat = "." in str(res)
                self.display_label["text"] = str(res)
            except ZeroDivisionError:
                self.display_label["text"] = "Erreur : division par 0"
                self.inErrorState = True
            except SyntaxError:
                self.display_label["text"] = "Erreur de syntaxe"
                self.inErrorState = True

    def erase_all(self):
        self.isFloat = False
        self.display_label.config(text="0")
        self.inErrorState = False

    def erase_last(self):
        if len(self.display_label['text']) > 1:
            if self.display_label["text"][-1] == ".":
                self.isFloat = False
            while self.display_label["text"][-1].isdigit() or self.display_label["text"][-1] == ".":
                self.display_label.config(text=self.display_label['text'][:-1])
                if self.display_label["text"] == "":
                    self.display_label["text"] = "0"
                    break
        else:
            self.erase_all()

    def add_symbol(self, symbol):
        if self.display_label["text"][-1].isdigit():
            self.display_label["text"] = self.display_label["text"]+symbol
            self.isFloat = False
        elif self.display_label["text"][-1] != ".":
            self.display_label["text"] = self.display_label["text"][:-1] + symbol

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
