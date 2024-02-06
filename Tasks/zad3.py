#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def red():
    label['text'] = 'красный'
    ent.delete(0, END)
    ent.insert(0, '#ff0000')

def orange():
    label['text'] = 'оранжевый'
    ent.delete(0, END)
    ent.insert(0, '#ff7d00')


def yellow():
    label['text'] = 'жёлтый'
    ent.delete(0, END)
    ent.insert(0, '#ffff00')

def green():
    label['text'] = 'Зелёный'
    ent.delete(0, END)
    ent.insert(0, '#00ff00')


def blue():
    label['text'] = 'голубой'
    ent.delete(0, END)
    ent.insert(0, '#007dff')


def dark_blue():
    label['text'] = 'синий'
    ent.delete(0, END)
    ent.insert(0, '#0000ff')


def purple():
    label['text'] = 'фиолетовый'
    ent.delete(0, END)
    ent.insert(0, '#7d00ff')


root = Tk()
root.geometry('180x100')


ent = Entry(width=20)
ent.pack()
label = Label(width=20, height=2, bg='white')
label.pack()
button1 = Button(width=2, height=2, bg='red', command=red)
button1.pack()
button1.place(x=10, y=55)
button2 = Button(width=2, height=2, bg='orange', command=orange)
button2.pack()
button2.place(x=30, y=55)
button3 = Button(width=2, height=2, bg='yellow', command=yellow)
button3.pack()
button3.place(x=50, y=55)
button4 = Button(width=2, height=2, bg='green', command=green)
button4.pack()
button4.place(x=70, y=55)
button5 = Button(width=2, height=2, bg='blue', command=blue)
button5.pack()
button5.place(x=90, y=55)
button6 = Button(width=2, height=2, bg='dark blue', command=dark_blue)
button6.pack()
button6.place(x=110, y=55)
button7 = Button(width=2, height=2, bg='purple', command=purple)
button7.pack()
button7.place(x=130, y=55)

root.mainloop()