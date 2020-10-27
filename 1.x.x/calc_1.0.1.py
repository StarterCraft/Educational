# Библиотека
import time
import math

language = int(input('Please select your language: 0 for English, 1 for Russian: '))
print()

if language == 1:

# Инструкция для пользователя
    print('''
Здравствуйте, уважаемый пользователь!
Данный универсальный калькулятор Calcullо́ v 1.0.1 умеет выполнять 12 различных операций,
сохранение/сброс результата вычисления.
Версия 1.0 исполняется с помоощью командной строки.
Для начала вычислений, пожалуйста, укажите числа и символ необходимой операции:

1 (+) — Сложение
2 (-) — Вычитание
3 (*) — Умножение
4 (/) — Деление
5 (^) — Возведение в степень
6 (K) — Квадратный корень
7 (//) — Цельное деление
8.1 (%?) — Вычисление, сколько процентов составляет a от b
8.2 (%+) — Вычисление, чему равно a + b% a
8.3 (%-) — Вычисление, чему равно a - b% a
9 (окр+) — Округление а в большую сторону
10 (окр-) — Округление а в меньшую сторону
''')

# Контейнеры функциональности
    check = bool(False)
    s = str()

    def wait():
          print('Выполнение операции, пожалуйста, подождите...')
          time.sleep(1)

    def border():
            print('''
-----
''')

    def reset():
        border()
        print('Сброс сессии...')
        border()

#Первоначальное ожидание
    time.sleep(2)
    print('''
Инициализация...
''')
    time.sleep(3)

# Запуск первого бесконечного цикла работы
    x = int(0)
    while x <= 1:
        
# Запрос исходных данных
        if check == True:
            print('Введите 0 в стрoку ниже для принудительного сброса сессии')
            b = float(input('Пожалуйста, введите второе число: '))
            if b == 0:
                reset()
                a = 0
                a = float(input('Пожалуйста, введите первое число: '))
                s = str(input('Пожалуйста, введите код необходимой функции: '))
                b = float(input('Пожалуйста, введите второе число: '))
            else:
                s = str(input('Пожалуйста, введите код необходимой функции: '))
        else:
            a = float(input('Пожалуйста, введите первое число: '))
            s = str(input('Пожалуйста, введите код необходимой функции: '))
            b = float(input('Пожалуйста, введите второе число: '))
        
#Задаём функциональность и осуществляем выполнение операции
        r = float()
        if s == '+':
            print('Задана функция: сложение.')
     # Ожидание при выполнении операции
            wait()
            r = (a + b)
            print('Результат: ', r)
        else:
            if s == '-':
                print('Задана функция: вычитание.')
                wait()
                r = (a - b)
                print('Результат: ', r)
            else:
                 if s == '*':
                    print('Задана функция: умножение')
                    wait()
                    r = (a * b)
                    print('Результат: ', r)
                 else:
                    if s == '/':
                        print('Задана функция: деление')
                        wait()
                        r = (a / b)
                        print('Результат: ', r)
                    else:
                        if s == '^':
                            print('Задана функция: возведение a в степень b')
                            wait()
                            r = (math.pow(a, b))
                            print('Результат: ', r)
                        else:
                            if s == ('K' or 'k' or 'К' or 'к'):
                                 print('Задана функция: корень числа a')
                                 print('Внимание! При выполнении этой функции число b не учитывается.')
                                 wait()
                                 r = (math.sqrt(a))
                                 print('Результат: ', r)
                            else:
                                if s == '//':
                                    print('Задана функция: цельное деление')
                                    wait()
                                    r = (a // b)
                                    print('Результат: ', r)
                                else:
                                    if s == '%?':
                                        print('Задана функция: вычисление, сколько процентов составляет a от b')
                                        wait()
                                        r = ((a / b) * 100)
                                        print('Результат: ', r)
                                    else:
                                        if s == '%+':
                                            print('Задана функция: вычисление, чему равно a + b% a')
                                            wait()
                                            r = a + (a * (b / 100))
                                            print('Результат: ', r)
                                        else:
                                            if s == '%-':
                                                 print('Задана функция: вычисление, чему равно a - b% a')
                                                 wait()
                                                 r = a - (a * (b /100))
                                                 print('Результат: ', r)
                                            else:
                                                if s == 'окр+':
                                                    print('Задана функция: округление а в большую сторону')
                                                    print('Внимание! При выполнении этой функции число b не учитывается.')
                                                    wait()
                                                    r = math.ceil(a)
                                                    print('Результат: ', r)
                                                else:
                                                    if s == 'окр-':
                                                         print('Задана функция: округление а в меньшую сторону')
                                                         print('Внимание! При выполнении этой функции число b не учитывается.')
                                                         wait()
                                                         r = math.floor(a)
                                                         print('Результат: ', r)

#Сохранить или удалить?
        sod = str(input('''Вы можете сохранить результат этой операции для продолжения действий с ним, не сохранять
или завершить работу калькулятора.
Y — сохранение, N — сброс калькулятор. Ваш выбор: '''))
        #Пользователь продолжает сессию калькулятора
        if sod == ('Y' or 'y' or 'У' or 'у'):
                a = r
                check = True
                continue
        else:
            reset()
            continue
else:
    # User guidance
    print('''
Hello user!
This universal calculator Calcullо́ v 1.0.1 can perform 12 different operations,
saving / resetting the calculation result.
Version 1.0 is executed using the command line.
To start calculations, please insert the numbers and symbol of the required operation:

1 ( + ) — Addition
2 ( - ) — Subtraction
3 ( * ) — Multiplication
4 ( / ) — Division
5 ( ^ ) - Exponentiation
6 (K) - Square root
7 (//) — Whole division
8.1 (%?) - Calculate how much percent is "a" from "b"
8.2 (%+) - Calculation of what "a" + b% "a" is equal to
8.3 (%-) - Calculation of what "a" - b% "a" is equal to
9 (rnd+) - Rounding "a" up
10 (rnd-) - Rounding "a" down
''')

# Features' containers
    check = bool(False)
    s = str()

    def wait():
          print('Calculating, please wait...')
          time.sleep(1)

    def border():
            print('''
-----
''')

    def reset():
        border()
        print('Reseting Calcullо́...')
        border()

# Startup
    time.sleep(2)
    print('''
Initialization...
''')
    time.sleep(3)

# Infinitive cycle of the calculator
    x = int(0)
    while x <= 1:
        
# Input
        if check == True:
            print('Insert "0" below to reset Calcullо́')
            b = float(input('Insert the "b" number: '))
            if b == 0:
                time.sleep(1)
                reset()
                time.sleep(1)
                a = 0
                a = float(input('Insert the "a" number: '))
                s = str(input('Insert the function symbol: '))
                b = float(input('Insert the "b" number: '))
            else:
                s = str(input('Insert the function symbol: '))
        else:
            a = float(input('Insert the "a" number: '))
            s = str(input('Insert the function symbol: '))
            b = float(input('Insert the "b" number: '))
        
#Задаём функциональность и осуществляем выполнение операции
        r = float()
        if s == '+':
            print('Selected: addition')
     # Ожидание при выполнении операции
            wait()
            r = (a + b)
            print('Result: ', r)
        else:
            if s == '-':
                print('Selected: substraction.')
                wait()
                r = (a - b)
                print('Result: ', r)
            else:
                 if s == '*':
                    print('Selected: multiplication')
                    wait()
                    r = (a * b)
                    print('Result: ', r)
                 else:
                    if s == '/':
                        print('Selected: division')
                        wait()
                        r = (a / b)
                        print('Result: ', r)
                    else:
                        if s == '^':
                            print('Selected: Exponentiation')
                            wait()
                            r = (math.pow(a, b))
                            print('Result: ', r)
                        else:
                            if s == ('K' or 'k'):
                                 print('Selected: "a" square root')
                                 print('Warning: while this operation the "b" value is being ignored.')
                                 wait()
                                 r = (math.sqrt(a))
                                 print('Result: ', r)
                            else:
                                if s == '//':
                                    print('Selected: whole division')
                                    wait()
                                    r = (a // b)
                                    print('Result: ', r)
                                else:
                                    if s == '%?':
                                        print('Selected: calculation how much percent is "a" from "b"')
                                        wait()
                                        r = ((a / b) * 100)
                                        print('Result: ', r)
                                    else:
                                        if s == '%+':
                                            print('Selected: calculation of what "a" + b% "a" is equal to')
                                            wait()
                                            r = a + (a * (b / 100))
                                            print('Result: ', r)
                                        else:
                                            if s == '%-':
                                                 print('Selected: calculation of what "a" - b% "a" is equal to')
                                                 wait()
                                                 r = a - (a * (b /100))
                                                 print('Result: ', r)
                                            else:
                                                if s == 'rnd+':
                                                    print('Selected: rounding "a" up')
                                                    print('Warning: while this operation the "b" value is being ignored.')
                                                    wait()
                                                    r = math.ceil(a)
                                                    print('Result: ', r)
                                                else:
                                                    if s == 'rnd-':
                                                         print('Selected: rounding "a" down.')
                                                         print('Warning: while this operation the "b" value is being ignored.')
                                                         wait()
                                                         r = math.floor(a)
                                                         print('Result: ', r)

#Save or delete?
        sod = str(input('''You can save the result of this operation to continue working with it, delete it
or shut down the calculator.
Y — save result, N — reset the calculator. Your choice: '''))
        #User saves the result
        if sod == ('Y' or 'y' or 'У' or 'у'):
                a = r
                check = True
                continue
        else:
            reset()
            continue