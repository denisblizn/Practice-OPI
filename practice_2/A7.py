x1 = int(input('Введите значение x1\n'))
y1 = int(input('Введите значение y1\n'))
x2 = int(input('Введите значение x2\n'))
y2 = int(input('Введите значение y2\n'))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("White")
else:
    print("Black")