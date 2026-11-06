import random
import time

all_time = 0
prav_answer = 0
total_examples = (random.randint(1, 10))

for i in range(total_examples):
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    correct_answer = round(num1 * num2, 2)

    start_time = time.time()
    
    while True: 
        try: 
            user_answer = int(input(f"{num1} * {num2} = ")) 
            break
        except ValueError:
            print("Пожалуйста, введите целое число!") 

    time_spend = time.time() - start_time
    all_time += time_spend

    if user_answer == correct_answer:
        print(f'Правильно. Время: {round(time_spend, 2)}')
        prav_answer += 1
    else:
        print(f'Ошибка. Правильно: {correct_answer}, Время: {round(time_spend, 2)}')

credn_time = all_time / total_examples
percent_correct = (prav_answer / total_examples) * 100

total_examples = print(f'Кол-во примеров: {total_examples}')
all_time = print(f'Общее время: {round(all_time, 2)}')
credn_time = print(f'Среднее время: {round(credn_time, 2)}')
prav_answer = print(f'Правильных ответов: {prav_answer}')
percent_correct = print(f'Процент верных ответов: {round(percent_correct, 1)}%')