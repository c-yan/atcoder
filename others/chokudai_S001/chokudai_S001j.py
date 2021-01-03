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


N, *a = map(int, open(0).read().split())

bit = BinaryIndexedTree(N + 1)

result = 0
for x in a:
    result += bit.range_sum(x + 1, N + 1)
    bit.add(x, 1)
print(result)
