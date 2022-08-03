from random import *

print('Вас приветствует "Шифр Цезаря"')

def answer(t, a1, b1):
    print(t)
    while True:
        a = input().lower()
        if a == a1:
            return True
        elif a == b1:
            return False

