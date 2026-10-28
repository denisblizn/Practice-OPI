pred = int(input('Введите количество за прошлый месяц'))
curr = int(input('Введите количество за текущий месяц'))

if curr >= pred:
    obj = curr - pred
else:
    obj = (10000 - pred) + curr

if obj <= 300:
    cost = 21.00
    remain_obj = 0
else:
    cost = 21.00
    remain_obj = obj - 300

if remain_obj > 0:
    if remain_obj <= 300:
        cost += remain_obj * 0.06
        remain_obj = 0
    else:
        cost += 300 * 0.06
        remain_obj -= 300

if remain_obj > 0:
    if remain_obj <= 200:
        cost += remain_obj * 0.04
        remain_obj = 0
    else:
        cost += 200 * 0.04
        remain_obj -= 200

if remain_obj > 0:
    cost += remain_obj * 0.025



if obj > 0:
    price = cost / obj
else:
    price = 0.0

print('Использовано газа за текущий месяц:', obj, 'куб. м')
print(f'К оплате: {cost:.2f}')
print(f'Средняя цена: {price:.2f}')
