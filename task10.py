# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
coin_n = int(input("Введите количество монеток "))
coin_front = 0
coin_back = 0
for i in range(coin_n):
    full_coin = randint(0, 1)
    print(full_coin)
    if full_coin == 1:
        coin_front += 1
    else:
        coin_back +=1
if coin_front > coin_back:
    print(f"ОРЕЛ! Надо перевернуть {coin_back}")
else:
    print(f"РЕШКА! Надо перевернуть {coin_front}")
