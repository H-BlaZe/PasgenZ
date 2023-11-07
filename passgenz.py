import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip


def passDisplay(pwd):
    global passWin
    passWin = tk.Tk()
    passWin.title("PasgenZ by H_BlaZe")
    passWin.geometry("200x200")
    passLabel = tk.Label(passWin, text=pwd)
    passLabel.pack(padx=20, pady=20)
    copy = tk.Button(passWin, text="Copy to clipboard", command=lambda: pyperclip.copy(pwd))
    copy.pack()
    regen = tk.Button(passWin, text="Regenerate", command=lambda: brain(statBoth, statNum, statSpcl))
    regen.pack()
    back = tk.Button(passWin, text="Back", command=passWin.destroy)
    back.pack()


def brain(statBoth, statNum, statSpcl):
    try:
        passWin.destroy()
    except:
        print("NEW")

    low = list(string.ascii_lowercase)
    upp = list(string.ascii_uppercase)
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    spcl = ["(", ")", "[", "]", "#", "&", "_", "!"]
    pwd = ""
    case = [0]
    usedcase = []

    if statBoth.get():
        case.append(1)
    if statNum.get():
        case.append(2)
    if statSpcl.get():
        case.append(3)

    print(LenBox.get())

    for i in range(int(LenBox.get())):
        indexCase = random.randint(0, len(case) - 1)
        alphIndex = random.randint(0, 25)
        if case[indexCase] == 0:
            pwd += low[alphIndex]
            if 0 not in usedcase:
                usedcase.append(0)
        elif case[indexCase] == 1:
            pwd += upp[alphIndex]
            if 1 not in usedcase:
                usedcase.append(1)
        elif case[indexCase] == 2:
            numIndex = random.randint(0, 8)
            pwd += num[numIndex]
            if 2 not in usedcase:
                usedcase.append(2)
        else:
            spclIndex = random.randint(0, 7)
            pwd += spcl[spclIndex]
            if 3 not in usedcase:
                usedcase.append(3)

    usedcase.sort()

    print(usedcase, "---------", case)

    if usedcase == case:
        print(pwd)
        passDisplay(pwd)
    else:
        print("NO")
        print(pwd)
        print("NO")
        brain(statBoth, statNum, statSpcl)


def menu():
    global mainWin
    mainWin = tk.Tk()
    mainWin.title("PasgenZ by H_BlaZe")
    mainWin.geometry("500x200")
    global statBoth
    statBoth = tk.BooleanVar()
    bothCheck = tk.Checkbutton(mainWin, variable=statBoth, text="Use both Uppercase and Lowercase")
    bothCheck.pack()
    global statNum
    statNum = tk.BooleanVar()
    numCheck = tk.Checkbutton(mainWin, variable=statNum, text="Use numbers")
    numCheck.pack()
    global statSpcl
    statSpcl = tk.BooleanVar()
    spclCheck = tk.Checkbutton(mainWin, variable=statSpcl, text="Use special characters")
    spclCheck.pack()

    txt1 = tk.Label(mainWin, text="Choose Length:")
    txt1.pack()
    global LenBox
    LenBox = ttk.Combobox(mainWin, state="readonly")
    LenBox.pack(padx=10, pady=10)

    values = [str(i) for i in range(4, 33)]

    LenBox["values"] = values

    submit = tk.Button(mainWin, text="Generate", command=lambda: brain(statBoth, statNum, statSpcl))
    submit.pack()

    mainWin.mainloop()


menu()
