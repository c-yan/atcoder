# Disjoint sparse table (GCD)
from math import gcd


class DisjointSparseTable:
    _f = None
    _data = None
    _lookup = None

    def __init__(self, a, f):
        self._f = f
        b = 0
        while (1 << b) <= len(a):
            b += 1
        _data = [[0] * len(a) for _ in range(b)]
        _data[0] = a[:]
        for i in range(1, b):
            shift = 1 << i
            for j in range(0, len(a), shift << 1):
                t = min(j + shift, len(a))
                _data[i][t - 1] = a[t - 1]
                for k in range(t - 2, j - 1, -1):
                    _data[i][k] = f(a[k], _data[i][k + 1])
                if t >= len(a):
                    break
                _data[i][t] = a[t]
                r = min(t + shift, len(a))
                for k in range(t + 1, r):
                    _data[i][k] = f(_data[i][k - 1], a[k])
        self._data = _data
        _lookup = [0] * (1 << b)
        for i in range(2, len(_lookup)):
            _lookup[i] = _lookup[i >> 1] + 1
        self._lookup = _lookup

    def query(self, start, stop):
        stop -= 1
        if start >= stop:
            return self._data[0][start]
        p = self._lookup[start ^ stop]
        return self._f(self._data[p][start], self._data[p][stop])



N = int(input())
A = list(map(int, input().split()))

st = DisjointSparseTable(A, gcd)

result = st.query(1, N)
for i in range(1, N - 1):
    result = max(result, gcd(st.query(0, i), st.query(i + 1, N)))
result = max(result, st.query(0, N - 1))
print(result)
