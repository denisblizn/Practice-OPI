import string

password = input('Введите пароль содержащий 8 символов:')
allowed_specials = string.punctuation

if len(password) < 8:
    print('Длина пароля не равна 8')

errors = []

up = False
low = False
numb = False
special = False
invalid = False

for i in password:
    if i.isupper():
        up = True
    elif i.islower():
        low = True
    elif i.isdigit():
        numb = True
    elif i in allowed_specials:
        special = True
    else:
        invalid = True

if not up:
    errors.append('Отсутсвует заглавная буква')
if not low:
    errors.append('Отсутсвует строчная буква')
if not numb:
    errors.append('Отсуствует цифра')
if not special:
    errors.append('Отсуствует специальный символ')
if invalid:
    errors.append('В пароле недопустимый симовл')

if not errors:
    print('Надежный пароль')
else:
    print(errors)