s = input()
a = s.find('f')
b = (s.find('f', a + 1))
if a == -1:
    print(-2)
else:
    print(b)
