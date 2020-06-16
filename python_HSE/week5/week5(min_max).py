# В списке все элементы попарно различны.
# Поменяйте местами минимальный и
# максимальный элемент этого списка.


f_list = list(map(int, input().split()))
min = f_list[0]
imin = 0
max = f_list[0]
imax = 0
i = 0
while i < len(f_list):
    if f_list[i] < min:
        min = f_list[i]
        imin = i
    elif f_list[i] > max:
        max = f_list[i]
        imax = i
    i += 1
f_list[imin] = max
f_list[imax] = min
print(*f_list)
