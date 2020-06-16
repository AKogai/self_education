n = int(input())
if n == 1 or n % 10 == 1 and n != 11:
    print(n, 'korova')
elif n % 10 >= 2 and n % 10 <= 4 and (n < 12 or n > 20):
    print(n, 'korovy')
else:
    print(n, 'korov')
