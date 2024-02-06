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
root.geometry('200x350')


ent = Entry(width=20)
ent.pack()
label = Label(width=20, height=2, bg='white')
label.pack()
Button(width=20, height=2, bg='red', command=red).pack()
Button(width=20, height=2, bg='orange', command=orange).pack()
Button(width=20, height=2, bg='yellow', command=yellow).pack()
Button(width=20, height=2, bg='green', command=green).pack()
Button(width=20, height=2, bg='blue', command=blue).pack()
Button(width=20, height=2, bg='dark blue', command=dark_blue).pack()
Button(width=20, height=2, bg='purple', command=purple).pack()

root.mainloop()
