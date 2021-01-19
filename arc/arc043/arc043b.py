from operator import add


class DisjointSparseTable:
    def __init__(self, a, f):
        b = 0
        while (1 << b) <= len(a):
            b += 1
        data = [[0] * len(a) for _ in range(b)]
        data[0] = a[:]
        for i in range(1, b):
            shift = 1 << i
            for j in range(0, len(a), shift << 1):
                t = min(j + shift, len(a))
                data[i][t - 1] = a[t - 1]
                for k in range(t - 2, j - 1, -1):
                    data[i][k] = f(a[k], data[i][k + 1])
                if t >= len(a):
                    break
                data[i][t] = a[t]
                r = min(t + shift, len(a))
                for k in range(t + 1, r):
                    data[i][k] = f(data[i][k - 1], a[k])
        lookup = [0] * (1 << b)
        for i in range(2, len(lookup)):
            lookup[i] = lookup[i >> 1] + 1
        self._f = f
        self._data = data
        self._lookup = lookup

    def query(self, start, stop):
        data = self._data
        stop -= 1
        if start >= stop:
            return data[0][start]
        p = self._lookup[start ^ stop]
        return self._f(data[p][start], data[p][stop])


m = 1000000007
D_MAX = 10 ** 5

N, *D = map(int, open(0).read().split())
D.sort()

t = [0] * (D_MAX + 1)
for d in D:
    t[d] += 1
st = DisjointSparseTable(t, add)

A = [0] * (D_MAX + 1)
for d in D:
    if d * 2 > D_MAX:
        break
    A[d] = t[d] * st.query(d * 2, D_MAX + 1)
st2 = DisjointSparseTable(A, add)

result = 0
for d in D:
    if d * 2 > D_MAX:
        break
    result += st.query(0, d // 2 + 1) * st2.query(d * 2, D_MAX + 1)
    result %= m
print(result)
