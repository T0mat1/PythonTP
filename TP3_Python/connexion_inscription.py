# -*- coding: utf-8 -*-
# TP3 Python - Emeric PAIN & Thomas ROSSI

from tkinter import *


def display_popup_inscription():
    window = Toplevel()
    window.grab_set()
    window.wm_title("Inscription")
    window.geometry("300x150+500+300")
    window.wm_resizable(False, False)
    Label(window, text="Ajout d'un couple login/password").pack()
    Label(window, text="Entrez votre login").pack()
    loginToVerify = Entry(window, show="*")
    loginToVerify.pack()
    Label(window, text="Entrez votre mot de passe").pack()
    passwordToVerify = Entry(window)
    passwordToVerify.pack()
    Button(window, width=str(10), height=str(2), text="Valider", command=lambda: do_inscription(passwordToVerify),
           borderwidth=1).pack()
    window.mainloop()
    try:
        window.grab_release()
    except TclError:
        pass


def check_connexion(login, password):
    print(login)
    print(password)


def do_inscription(loginToVerify, passwordToVerify):
    print(loginToVerify)
    print(passwordToVerify)


class ConnexionInscription:

    def __init__(self):
        self.window = Tk()
        self.window.title("Connexion & Inscription")
        self.window.wm_resizable(False, False)
        self.window.geometry('300x80+500+200')
        self.rows = []
        self.rows.append(Frame(self.window, bd=0))
        self.rows[0].pack()
        Button(self.rows[0], width=str(10), height=str(2), text="Connexion",
               command=lambda: self.display_popup_connexion(),
               borderwidth=1).grid(row=0, column=0)
        Button(self.rows[0], width=str(10), height=str(2), text="Inscription",
               command=lambda: display_popup_inscription(), borderwidth=1).grid(row=0, column=1)
        self.window.mainloop()

    def display_popup_connexion(self):
        window = Toplevel()
        window.grab_set()
        window.wm_title("Connexion")
        window.geometry("300x150+500+300")
        window.wm_resizable(False, False)
        Label(window, text="Vérification d'un couple login/password").pack()
        Label(window, text="Entrez votre login").pack()
        login = Entry(window)
        login.pack()
        self.login = login["text"]
        Label(window, text="Entrez votre mot de passe").pack()
        password = Entry(window, show="*")
        password.pack()
        self.password = password["text"]
        Button(window, width=str(10), height=str(2), text="Valider",
               command=lambda: check_connexion(self.login, self.password),
               borderwidth=1).pack()
        window.mainloop()
        try:
            window.grab_release()
        except TclError:
            pass


if __name__ == "__main__":
    ConnexionInscription()
