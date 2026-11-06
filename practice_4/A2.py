
figura = input('Выберите фигуру (прямоугольник, треугольник, рамка): ')
symbol = input('Введите символ который хотите использовать: ')

if figura == 'прямоугольник':
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))
    for i in range(n):
        for j in range(m):
            print(symbol, end='')
        print()
    print()

elif figura == 'треугольник':
    n = int(input('Введите количество строк: '))
    for i in range(1, n + 1):
        for j in range(i):
            print(symbol, end='')
        print()
    print()

elif figura == 'рамка':
    n = int(input('Введите количество строк: '))   
    m = int(input('Введите количество столбцов: '))
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(symbol, end='')
            else:
                print(' ', end='')
        print()
    print()

else:
    print('Неверное название фигуры \n')