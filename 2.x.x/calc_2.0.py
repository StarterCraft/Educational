# Библиотеки
import math
from time import sleep
from tkinter import *
from tkinter import messagebox

# Окно и его свойства
win = Tk()
win.title('Calcullo v 2.0.0')
win.geometry('400x550+1000+200')
win.resizable(width = False, height = False)
win.config(bg='black')

num = float()
stringVar = StringVar()

themeToGet = int()

menu = Menu(win)
win.config(menu = menu)

def settings():
    global themeToGet
    theme = int()

    SettingsWindow = Tk()
    SettingsWindow.title('Cacullo - Параметры')
    SettingsWindow.geometry('200x255+1000+200')
    SettingsWindow.resizable(width = False, height = False)
    SettingsWindow.config(bg='black')

    setLabel1 = Label(SettingsWindow, text = 'Тема калькулятора', font = 'tahoma 12', fg = 'white').grid(row = 0, column = 0, sticky = W)
    setRb1 = Radiobutton(SettingsWindow, text = 'Тёмная', font = 'tahoma 12', fg = 'white', variable = theme, value = 'Dark', command = lambda x = 1: theme(x)).grid(row = 1, column = 0, sticky = W)
    setRb2 = Radiobutton(SettingsWindow, text = 'Светлая', font = 'tahoma 12', fg = 'white', variable = theme, value = 'Light', command = lambda x = 2: theme(x)).grid(row = 1, column = 0, sticky = W)

    theme = themeToGet
    

branch1 = Menu(menu)
menu.add_cascade(label = 'Настройки', menu = branch1)
branch1.add_command(label = 'Параметры', command = settings())
branch1.add_command(label = 'Отладка')


branch2 = Menu(menu)
menu.add_cascade(label = 'О нас', menu = branch2)
branch2.add_command(label = 'О нас')
branch1.add_command(label = 'Помощь')

menu.add_command(label = 'Abort')

def main_calc(i):
    pass

entry = Entry(win, text = stringVar, justify = RIGHT, font = 'segoe_ui 40', bg = 'black', fg = 'white', width = 13)
entry.grid(row = 0, column = 0, columnspan = 5, padx = 8, pady = 8)

# Кнопки
bt_text = ['О+', 'О-', '%?', '%+', '%-',
           '(', ')', '|x|', '<', '/',
           '7', '8', "9", '√', '×',
           '4', '5', '6', '^', '-',
           '1', '2', '3', '', '+',
           '.', '0', '+/-', '', '=']


bt_widgets = []


_row = 1
_column = 0


def calc(i):
    global entry

    if i in '01234567890()+-/√^.':
        entry.insert(END, i)
    elif i == '<':
        entry.delete(len(entry.get())-1)
    elif i == '√':
        entry.insert(END, '**(0.5)')
    elif i == '×':
        entry.insert(END, '*')
    elif i == '^':
        entry.insert(END, '**')
    elif i == '=':
        try:
            result = eval(entry.get())
            entry.insert(END, ' = ' + str(result))
        except SyntaxError:
            messagebox.showerror('Unexpected error', 'Fatal error')


for i in bt_text:

    _btn = Button(win, text = i, width = 4, font = 'tahoma 20', bg = 'black', fg = 'snow', bd = 3, command = calc(i))
    _btn.grid(row = _row, column = _column, padx = 1, pady = 1)
    bt_widgets.append(_btn)

    #
    _column += 1
    if _column > 4:
        _column = 0
        _row = (_row + 1)


def switchThemes(themeid):
    themeid = themeToGet
    if themeid == 1:
        win.config(bg = 'black')
        for i in range(len(bt_widgets)):
            bt_widgets[i].config(bg = 'black', fg = 'white')
    elif themeid == 2:
        win.config(bg = 'snow')
        for i in range(len(bt_widgets)):
            bt_widgets[i].config(bg = 'white', fg = 'black')


win.mainloop()