from math import sqrt
a, b = input().split()
n = int(a + b)
if sqrt(n) == int(sqrt(n)):
    print('Yes')
else:
    print('No')
