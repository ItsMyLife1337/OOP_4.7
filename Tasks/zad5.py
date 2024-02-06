#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def change():
    if r_var.get() == 1:
        label1['text'] = '89624523322'
    elif r_var.get() == 2:
        label1['text'] = '89657774566'
    elif r_var.get() == 3:
        label1['text'] = '89993346899'


root = Tk()
root.geometry('150x150')

r_var = IntVar()
r_var.set(0)

r1 = Radiobutton(text='Вася', command=change,
                 variable=r_var, value=1,
                 indicatoron=0)
r2 = Radiobutton(text='Петя', command=change,
                 variable=r_var, value=2,
                 indicatoron=0)
r3 = Radiobutton(text='Маша', command=change,
                 variable=r_var, value=3,
                 indicatoron=0)

label1 = Label(width=10, height=5)

r1.pack()
r1.place(x=10, y=35)
r2.pack()
r2.place(x=10, y=60)
r3.pack()
r3.place(x=10, y=85)
label1.pack()
label1.place(x=55, y=35)

root.mainloop()
