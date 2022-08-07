direction = ''
dictionary = ''
CHAR = '~!@#$%^&*()_-=+-/*"|{}[],. \'1234567890'
TEXT = ''
step = 0

print('Вас приветствует "Шифр Цезаря"')

print('Выберите направление(шифрование/дешифровка)')
while True:
    t = input().lower()

    if t == 'шифрование':
        direction = t
        break

    elif t == 'дешифровка':
        direction = t
        dirflag = True
        break

print('Выберите язык алфавита(русский/английский)')
while True:
    t = input().lower()

    if t == 'русский':
        dictionary = t
        break
    elif t == 'английский':
        dictionary = t
        break

print('укажите шаг:')
while True:
    t = input()
    for i in range(len(t)):
        if t[i] not in '0123456789' or t == '':
            break
    else:
        step = int(t)
        break

print('Введите ваш текст')
TEXT = input()

result = ''
if direction == 'дешифровка':
    for i in range(len(TEXT)):
        if TEXT[i] not in CHAR:
            if dictionary == 'английский':
                if TEXT[i].isupper():
                    if ord(TEXT[i]) - step < 65:
                        result += chr(ord(TEXT[i]) - step + 26)
                    else:
                        result += chr(ord(TEXT[i]) - step)
                else:
                    if ord(TEXT[i]) - step < 97:
                        result += chr(ord(TEXT[i]) - step + 26)
                    else:
                        result += chr(ord(TEXT[i]) - step)
            else:
                if TEXT[i].isupper():
                    if ord(TEXT[i]) - step < 1040:
                        result += chr(ord(TEXT[i]) - step + 32)
                    else:
                        result += chr(ord(TEXT[i]) - step)

                else:
                    if ord(TEXT[i]) - step < 1072:
                        result += chr(ord(TEXT[i]) - step + 32)
                    else:
                        result += chr(ord(TEXT[i]) - step)

        else:
            result += TEXT[i]

else:
    for i in range(len(TEXT)):
        if TEXT[i] not in CHAR:
            if dictionary == 'английский':
                if TEXT[i].isupper():
                    if ord(TEXT[i]) + step > 90:
                        result += chr((ord(TEXT[i]) + step + 65) % 91)
                    else:
                        result += chr(ord(TEXT[i]) + step)
                else:
                    if ord(TEXT[i]) + step > 122:
                        result += chr((ord(TEXT[i]) + step + 97) % 123)
                    else:
                         result += chr(ord(TEXT[i]) + step)
            else:
                if TEXT[i].isupper():
                    if ord(TEXT[i]) + step > 1071:
                        result += chr((ord(TEXT[i]) + step + 1040) % 1072)
                    else:
                        result += chr(ord(TEXT[i]) + step)

                else:
                    if ord(TEXT[i]) + step > 1103:
                        result += chr((ord(TEXT[i]) + step + 1072) % 1104)
                    else:
                        result += chr(ord(TEXT[i]) + step)

        else:
            result += TEXT[i]

print(result)