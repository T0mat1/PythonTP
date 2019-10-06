# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("Calculatrice")
    fenetre.wm_resizable(False, False)
    #fenetre.geometry('300x450+400+400')

    def clicked(x):
        print("The button clicked is: "+x)

    for col in range(3):
        for line in range(3):
            Button(fenetre, height=3, width=5, text=str(3*line+col+1), command=partial(clicked, str(3*line+col+1)), borderwidth=3).grid(row=line, column=col)
    Button(fenetre, height=3, width=5, text="0", command=partial(clicked, "0"), borderwidth=3).grid(row=3, column=0)
    Button()

    fenetre.mainloop()