# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу
# с центром (xc, yc) и радиусом r. Если точка
# принадлежит кругу, выведите слово YES, иначе
# выведите слово NO. Решение должно содержать
# функцию IsPointInCircle(x, y, xc, yc, r),
# возвращающую True, если точка принадлежит
# кругу и False, если не принадлежит. Основная
# программа должна считать координаты точки,
# вызвать функцию IsPointInCircle и в зависимости
# от возвращенного значения вывести на экран необходимое
# сообщение. Функция IsPointInCircle не должна
# содержать инструкцию if.
from math import sqrt


def IsPointInCircle(x, y, xc, yc, r):
    a = sqrt((xc - x) * (xc - x) + (yc - y) * (yc - y)) <= r
    return a

x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
