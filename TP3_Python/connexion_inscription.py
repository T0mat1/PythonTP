# -*- coding: utf-8 -*-
# TP3 Python - Emeric PAIN & Thomas ROSSI

from tkinter import *
import hashlib


def hash_password(password_to_hash):
    return hashlib.sha256(password_to_hash.encode()).hexdigest()


def display_couple_identifiant_mdp_trouve(est_trouve):
    window = Toplevel()
    window.grab_set()
    window.geometry("300x50+500+300")
    window.wm_resizable(False, False)
    if est_trouve:
        Label(window, text="Couple identifiant - mot de passe trouvé").pack()
    else:
        Label(window, text="Couple identifiant - mot de passe non trouvé").pack()
    window.mainloop()


def display_confirmation_inscription():
    window = Toplevel()
    window.grab_set()
    window.geometry("300x50+500+300")
    window.wm_resizable(False, False)
    Label(window, text="Couple identifiant - mot de passe inscrit").pack()
    window.mainloop()


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
               command=lambda: self.display_popup_inscription(), borderwidth=1).grid(row=0, column=1)
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
        Label(window, text="Entrez votre mot de passe").pack()
        password = Entry(window, show="*")
        password.pack()
        Button(window, width=str(10), height=str(2), text="Valider",
               command=lambda: self.check_connexion(login.get(), password.get()),
               borderwidth=1).pack()
        window.mainloop()
        try:
            window.grab_release()
        except TclError:
            pass

    def display_popup_inscription(self):
        window = Toplevel()
        window.grab_set()
        window.wm_title("Inscription")
        window.geometry("300x150+500+300")
        window.wm_resizable(False, False)
        Label(window, text="Ajout d'un couple login/password").pack()
        Label(window, text="Entrez votre login").pack()
        login_to_verify = Entry(window)
        login_to_verify.pack()
        Label(window, text="Entrez votre mot de passe").pack()
        password_to_verify = Entry(window, show="*")
        password_to_verify.pack()
        Button(window, width=str(10), height=str(2), text="Valider",
               command=lambda: self.do_inscription(login_to_verify.get(), password_to_verify.get()),
               borderwidth=1).pack()
        window.mainloop()
        try:
            window.grab_release()
        except TclError:
            pass

    @staticmethod
    def check_connexion(login, password):
        assert (login != "" and password != ""), "Login ou mot de passe vide"
        user_pwd_found = False
        salage_password = password + login + password[:2]
        with open("loginPassword.txt", "r") as f:
            file_content = f.readlines()
        for line in file_content:
            if (login + "/" + hash_password(salage_password) + "\n") == line:
                user_pwd_found = True
        display_couple_identifiant_mdp_trouve(user_pwd_found)

    @staticmethod
    def do_inscription(login_to_add, password_to_add):
        if login_to_add == "":
            raise Exception('Login vide')
        if password_to_add == "":
            raise Exception('Mot de passe vide')
        file = open("loginPassword.txt", "a")
        salage_password = password_to_add + login_to_add + password_to_add[:2]
        file.write(login_to_add + "/" + hash_password(salage_password) + "\n")
        file.close()
        display_confirmation_inscription()


if __name__ == "__main__":
    ConnexionInscription()
