from math import gcd
from functools import reduce
from itertools import combinations

N, *X = map(int, open(0).read().split())

s = {2, 3, 5, 37, 7, 41, 11, 43, 13, 47, 17, 19, 23, 29, 31}
result = 10 ** 18
for i in range(len(s)):
    for c in combinations(s, i + 1):
        a = reduce(lambda x, y: x * y, c)
        for x in X:
            if gcd(a, x) != 1:
                continue
            break
        else:
            result = min(result, a)
print(result)
