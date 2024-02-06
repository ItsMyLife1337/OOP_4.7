#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def str_to_sort_list():
    a = entry1.get()
    b = entry2.get()
    my_list = [a, b]
    return my_list


def minus(event):
    try:
        s = str_to_sort_list()
        difference = float(s[0]) - float(s[1])
        lab['text'] = difference
    except ValueError:
        lab['text'] = 'Неверный ввод данных!'


def plus(event):
    try:
        s = str_to_sort_list()
        summ = float(s[0]) + float(s[1])
        lab['text'] = summ
    except ValueError:
        lab['text'] = 'Неверный ввод данных!'


def multiplication(event):
    try:
        s = str_to_sort_list()
        multip = float(s[0]) * float(s[1])
        lab['text'] = multip
    except ValueError:
        lab['text'] = 'Неверный ввод данных!'


def segmentation(event):
    try:
        s = str_to_sort_list()
        segmentat = float(s[0]) / float(s[1])
        lab['text'] = segmentat
    except ValueError:
        lab['text'] = 'Неверный ввод данных!'


root = Tk()
root.geometry('150x200')

entry1 = Entry()
entry1.pack(padx=0, pady=6)
entry2 = Entry()
entry2.pack(padx=2, pady=6)

but = Button(text="+", width=50)
but.pack(padx=5, pady=1)
but1 = Button(text="-", width=50)
but1.pack(padx=5, pady=1)
but2 = Button(text="*", width=50)
but2.pack(padx=5, pady=1)
but3 = Button(text="/", width=50)
but3.pack(padx=5, pady=1)
lab = Label(width=50, bg='white', fg='black')

but.bind('<Button-1>', plus)
but1.bind('<Button-1>', minus)
but2.bind('<Button-1>', multiplication)
but3.bind('<Button-1>', segmentation)
but.pack()
lab.pack()
root.mainloop()
