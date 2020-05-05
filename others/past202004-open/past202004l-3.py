class SparseTable():
    _data = None
    _lookup = None
    _f = None

    def __init__(self, a):
        data = []
        lookup = []
        f = min
        b = 0
        while (1 << b) <= len(a):
            b += 1
        for _ in range(b):
            data.append([0] * (1 << b))
        data[0][:len(a)] = a
        for i in range(1, b):
            j = 0
            di = data[i]
            di1 = data[i - 1]
            while j + (1 << i) <= (1 << b):
                di[j] = f(di1[j], di1[j + (1 << (i - 1))])
                j += 1
        lookup = [0] * (len(a) + 1)
        for i in range(2, len(lookup)):
            lookup[i] = lookup[i >> 1] + 1
        self._data = data
        self._lookup = lookup
        self._f = f

    def query(self, start, stop):
        b = self._lookup[stop - start]
        db = self._data[b]
        return self._f(db[start], db[stop - (1 << b)])


N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

st = SparseTable(A)

result = []
i = 0
for k in range(K - 1, -1, -1):
    m = st.query(i, N - k * D)
    result.append(m)
    while A[i] != m:
        i += 1
    i += D
print(*result)
