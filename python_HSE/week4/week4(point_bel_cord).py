# Даны два действительных числа x и y.
# Проверьте, принадлежит ли точка с координатами (x,y)
# заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES,
# иначе выведите слово NO. (квадрат с шагом 1 вокруг 0)
# Решение должно содержать функцию IsPointInSquare(x, y),
# возвращающую True, если точка принадлежит квадрату и False,
# если не принадлежит. Основная программа должна считать
# координаты точки, вызвать функцию IsPointInSquare и в
# зависимости от возвращенного значения вывести на экран
# необходимое сообщение. Функция IsPointInSquare не должна
# содержать инструкцию if.


def IsPointInSquare(x, y):
    return (-1 <= x <= 1 and -1 <= y <= 1)

x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
