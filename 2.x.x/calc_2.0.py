# Библиотеки
import math
import time
from tkinter import *

# Окно, холст и его свойства
win = Tk()
win.title('Calcullo v 2.0.0')
win.geometry('400x550+1000+200')
win.config(bg='black')

def test():
    win.title('Кнопка нажата!')
    time.sleep(1)
    win.title('Calcullo v 2.0.0')

# Кнопка
testButton = Button(win, text='test', width=10, height=5, bg='grey', command=test, font='tahoma 18', activebackground='red')
testButton.place(x=200, y=200)

# Цикл обработки событий (последняя строка)
win.mainloop()
