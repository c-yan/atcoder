from math import gcd
from functools import reduce

N, *A = map(int, open(0).read().split())

def is_pairwise_coprime():
    t = [0] * (10 ** 6 + 1)
    for a in A:
        t[a] += 1

    c = 0
    for j in range(2, 10 ** 6 + 1, 2):
        c += t[j]
    if c > 1:
        return False

    for i in range(3, 10 ** 6 + 1, 2):
        c = 0
        for j in range(i, 10 ** 6 + 1, i):
            c += t[j]
        if c > 1:
            return False

    return True

if is_pairwise_coprime():
    print('pairwise coprime')
elif reduce(gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')
