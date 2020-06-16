# Отсортируйте данный массив, используя встроенную сортировку.

N = input()
A_list = list(map(int, input().split()))
A_list = sorted(A_list)
print(*A_list)
