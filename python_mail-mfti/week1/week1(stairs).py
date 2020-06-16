import sys


a = int(sys.argv[1])
for d in range(1, a + 1):
    print(' ' * (a - d) + '#' * d)
