packets = input('Введите данные: ')

count = 0

if len(packets) < 5:
    print('Неверное количество данных')

if not all(char in '01' for char in packets): 
        print("Неверный ввод. Используйте только символы '0' и '1'!") 

for packet in packets: 
        if packet == '0':
               count += 1



pac = len(packets)
lost_pac = count
precent_lost = (lost_pac / pac) * 100

max_lost = len(max(packets.split('1')))

if precent_lost <= 1:
    quality = ('Отличное качество')
elif precent_lost <= 5:
    quality = ('Удовлетворительное качество ')
elif precent_lost <= 10:
    quality = ('Удовлетворительное качество ')
elif precent_lost <= 20:
    quality = ('Плохое качество ')
else:
    quality = ('Критическое состояние сети ')



print(f'Общее количество пакетов: {pac}')
print(f'Количество потерянных пакетов: {lost_pac}')
print(f'Длина самой длинной последовательности потерянных пакетов: {max_lost}')
print(f'Процент потерь: {round(precent_lost, 1)}%')
print(f'Качество связи: {quality}')