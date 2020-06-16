a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
delta = a * d - b * c
delta_x = d * e - b * f
delta_y = a * f - c * e
y = delta_y / delta
x = delta_x / delta
print(float(x), float(y))
