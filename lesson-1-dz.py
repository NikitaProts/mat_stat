from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def arrangements(n, k):
    return int(factorial(n) / factorial(n - k))

#Задание 1
print(f'Все карты крести: {combinations(13, 4)  / combinations(52, 4)}')
print(f'Хотя бы один туз: {1 - combinations(48, 4) / combinations(52, 4)}')

#Задание 2
print(f'Вероятность открытия двери: {1 / combinations(10, 3)}')

#Задание 3
print(f'Вероятность что все детали будут окрашены: {(9 / 15) * (8/14) * (7 / 13)}')

#Задание 4
print(f'Вероятность выигрышных билетов: {(2/100) * (1/99) }')

#Задание 5
print(f'Первый спортсмен: {(0.81 * 1/3) / ((1/3 * 0.81) + (1/3 * 0.64) + (1/3 * 0.36))}')
print(f'Второй спортсмен: {(0.64 * 1/3) / ((1/3 * 0.81) + (1/3 * 0.64) + (1/3 * 0.36))}')
print(f'Третий спортсмен: {(0.36 * 1/3) / ((1/3 * 0.81) + (1/3 * 0.64) + (1/3 * 0.36))}')