# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть
# выведите два других числа p и q
# таких, что (n / m) = (p / q) и
# дробь (p / q) — несократимая.
# Решение оформите в виде функции
# ReduceFraction(n, m), получающая
# значения n и m и возвращающей кортеж
# из двух чисел: return p, q. Тогда
# вывод можно будет оформить как
# print(*ReduceFraction(n, m)).


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, (n % m))


def ReduceFraction(n, m):
    p = n // gcd(n, m)
    q = m // gcd(n, m)
    return p, q


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
