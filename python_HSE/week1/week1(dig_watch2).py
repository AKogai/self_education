N = int(input())
hrs = (N // 3600) % 24
minute = ((N % 3600) // 60)
secs = N % 60
print(hrs, ':', minute // 10, minute % 10, ':', secs // 10, secs % 10, sep='')
