# BIT (Binary indexed tree)
from sys import stdin
readline = stdin.readline


def bit_add(bit, i, x):
    i += 1
    n = len(bit)
    while i <= n:
        bit[i - 1] += x
        i += i & -i


def bit_sum(bit, i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i - 1]
        i -= i & -i
    return result


def query(bit, start, stop):
    if start == 0:
        return bit_sum(bit, stop - 1)
    else:
        return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


N, M = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])

bit = [0] * (N - 1)
result = 0
for a, b in ab:
    a, b = a - 1, b - 1
    if query(bit, a, b) != 0:
        continue
    result += 1
    bit_add(bit, b - 1, 1)
print(result)
