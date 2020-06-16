# Переставьте соседние элементы списка
# (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то
# последний элемент остается на своем месте.


f_list = list(map(int, input().split()))
i = 0
while i < len(f_list) - 1:
    f_list[i], f_list[i + 1] = f_list[i + 1], f_list[i]
    i += 2
print(*f_list)
