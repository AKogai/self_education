# Напишите программу, которая находит в массиве
# элемент, самый близкий по величине к данному
# числу. Формат ввода В первой строке задается
# одно натуральное число N, не превосходящее 1000
# – размер массива. Во второй строке содержатся N
# чисел – элементы массива (целые числа,
# не превосходящие по модулю 1000). В третьей строке
# вводится одно целое число x, не превосходящее по
# модулю 1000. Формат вывода Вывести значение
# элемента массива, ближайшее к x. Если таких
# чисел несколько, выведите любое из них


N = int(input())
list = list(map(int, input().split()))
x = int(input())
t = list[0]
i = 0
while i < len(list):
    if abs(x - list[i]) < abs(x - t):
        t = list[i]
    i += 1
print(t)
