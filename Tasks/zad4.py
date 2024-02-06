#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def open_file():
    filename = ent.get()
    with open(filename, 'r', encoding='utf-8') as file:
        text_inside = file.read()
        text.delete(END)
        text.insert(END, text_inside)


def change():
    filename = ent.get()
    text_inside = text.get(1.0, END + '-1c')  # Получаем текст с символом новой строки в конце
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text_inside + '\n')  # Добавляем символ новой строки


root = Tk()

ent = Entry(width=20)
ent.pack()

text = Text()
text.pack()
button1 = Button(text='Открыть', command=open_file)
button1.pack()
button2 = Button(text='Сохранить', command=change)
button2.pack()

root.mainloop()
