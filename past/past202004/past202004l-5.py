# Dosjoint sparse table (Min)
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

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

st = DisjointSparseTable(A, min)

result = []
i = 0
for k in range(K - 1, -1, -1):
    m = st.query(i, N - k * D)
    result.append(m)
    while A[i] != m:
        i += 1
    i += D
print(*result)
