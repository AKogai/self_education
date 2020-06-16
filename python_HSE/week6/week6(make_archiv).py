# Системный администратор вспомнил, что давно
# не делал архива пользовательских файлов.
# Однако, объем диска, куда он может поместить
# архив, может быть меньше чем суммарный объем
# архивируемых файлов. Известно, какой объем
# занимают файлы каждого пользователя. Напишите
# программу, которая по заданной информации о
# пользователях и свободному объему на архивном
# диске определит максимальное число пользователей,
# чьи данные можно поместить в архив. Формат ввода
# Программа получает на вход в одной строке число S
# – размер свободного места на диске (натуральное,
# не превышает 10000), и число N – количество
# пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого
# пользователя (натуральное, не превышает 1000),
# записанных каждое в отдельной строке. Формат вывода
# Выведите наибольшее количество пользователей, чьи
# данные могут быть помешены в архив.


s = [int(a) for a in input().split()]
k = 0
i = 1
N_list = []
while k + 1 <= s[1]:
    N_list.append(int(input()))
    k += 1
N_list.sort()
k = N_list[0]
while k <= s[0] and i < len(N_list):
    k += N_list[i]
    i += 1
if k > s[0]:
    print(i - 1)
else:
    print(i)
