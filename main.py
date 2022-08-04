from random import *

direction = ''
dictionary = ''
step = 0

print('Вас приветствует "Шифр Цезаря"')
print('Выберите направление(шифрование/дешифрование)')

while True:
    t = input().lower()

    if t == 'шифрование':
        direction = t
        break

    elif t == 'дешифрование':
        direction = t
        break

print('Выберите язык алфавита(русский/английский)')

while True:
    t = input().lower()

    if t == 'русский':
       dictionary = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    elif t == 'английский':
        dictionary = 'abcdefghijklmnopqrstuvwxyz '

print('укажите шаг:')
while True:
    t = input()
    for i in range(len(t)):
        if t[i] not in '0123456789':
            break
    else:
        step = int(t)
        break
