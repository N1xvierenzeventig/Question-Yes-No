from random import *
from tkinter import *
import time

root = Tk()
root.title = ("Question")
root.geometry("500x300")

def main():
    global Text2
    qwertyq= randint(-4, 5)
    pas = "No"

    if qwertyq < 0: #40% Chance
        pas = "No"
    elif qwertyq > 1: #40% Chance
        pas = "Yes"
    elif qwertyq == 0 or 1: #20% chance
        pas = "Try again"
    Text2 = Label(root, width= 10, text=pas, font=("American Type", 12))
    Text2.grid(row = 3, column = 1, sticky = "")
    Btn["state"] = DISABLED
    time.sleep(0.5)
    return delete()


def remove_text():
    Text2.destroy()
    Btn["state"] = NORMAL


def delete():
    MyEntry.delete(0, 'end')

def closewin():
    root.destroy()


qwertyq = randint(-4, 5)
pas = "No"

Text = Label(root, text = "Input ur question in", font =("Areal", 10))
Text.grid(row = 1, column = 1, sticky = "")

Text3 = Label(root, text = "                            ", font =("Areal", 10)).grid(row = 2, column = 0, sticky = "")


MyEntry= Entry(root, width = 30, font = ("Helvetica",10), bd = 15)
MyEntry.grid(row = 2, column = 1)

Btn = Button(root, text = "Press Button if u'r ready with question", font = ("American Type", 10), command = main)
Btn.grid(row = 4, column = 1, sticky = "e")

Btn2 = Button(root, text = "Retry", font = ("American Type", 10), command = remove_text)
Btn2.grid(row = 6, column = 1, sticky = "")

Btn3 = Button(root, text = "Leave program", font = ("American Type" , 10), command = closewin)
Btn3.grid(row = 8, column = 1, padx = 1, pady = 1,  sticky = "")


root.mainloop()


