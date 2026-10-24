A = int(input("Введите число А\n"))
B = int(input("Введите число B\n"))

if A < 1 or A > 1000 or B < 1 or B > 1000:
    print('Значения не подходят под условие')
elif A == B:
    print('Оба числа равны')
elif A < B:
    print(B)
else:
    print(A)