# BIT (Binary indexed tree)
from sys import stdin


class BinaryIndexedTree:
    def __init__(self, size):
        self._data = [0] * size

    def add(self, i, x):
        data = self._data
        i += 1
        n = len(data)
        while i <= n:
            data[i - 1] += x
            i += i & -i

    def _sum(self, stop):
        data = self._data
        result = 0
        i = stop
        while i > 0:
            result += data[i - 1]
            i -= i & -i
        return result

    def range_sum(self, start, stop):
        return self._sum(stop) - self._sum(start)


readline = stdin.readline

N, M = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])

bit = BinaryIndexedTree(N - 1)
result = 0
for a, b in ab:
    a, b = a - 1, b - 1
    if bit.range_sum(a, b) != 0:
        continue
    result += 1
    bit.add(b - 1, 1)
print(result)
