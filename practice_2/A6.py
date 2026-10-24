Time = int(input('Введите секунды\n'))
h = Time // 3600
m = (Time % 3600) // 60
s = Time % 60
print(h,':', m,':', s)