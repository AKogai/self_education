a, b, c = float(input()), float(input()), float(input())
s = float
h_p = float
h_p = (a + b + c) / 2
s = (h_p * (h_p - a) * (h_p - b) * (h_p - c)) ** 0.5
print(s)
