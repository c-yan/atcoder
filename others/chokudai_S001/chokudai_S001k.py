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

m = 1000000007

fac = [0] * (N + 1)
fac[0] = 1
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i
    fac[i] %= m

bit = BinaryIndexedTree(N + 1)
result = 1
for x in a:
    result += (x - 1 - bit.range_sum(1, x)) * \
        fac[N - 1 - bit.range_sum(1, N + 1)]
    result %= m
    bit.add(x, 1)
print(result)
