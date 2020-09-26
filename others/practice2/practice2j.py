from sys import stdin


class SegmentTree:
    def __init__(self, size, op, e):
        self._op = op
        self._e = e
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [e] * (t * 2 - 1)

    def __getitem__(self, key):
        return self._data[self._offset + key]

    def __setitem__(self, key, value):
        op = self._op
        data = self._data
        i = self._offset + key
        data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def build(self, iterable):
        op = self._op
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def query(self, start, stop):
        def iter_segments(data, l, r):
            while l < r:
                if l & 1 == 0:
                    yield data[l]
                if r & 1 == 0:
                    yield data[r - 1]
                l = l // 2
                r = (r - 1) // 2
        op = self._op
        it = iter_segments(self._data, start + self._offset,
                           stop + self._offset)
        result = self._e
        for v in it:
            result = op(result, v)
        return result


readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

st = SegmentTree(N - 1, max, -1)
st.build(A)

result = []
for _ in range(Q):
    q = readline()
    if q[0] in '13':
        T, X, V = map(int, q.split())
        if T == 1:
            st[X - 1] = V
        elif T == 3:
            ok = N + 1
            ng = X - 1
            while abs(ng - ok) > 1:
                m = (ok + ng) // 2
                if st.query(X - 1, m) >= V:
                    ok = m
                else:
                    ng = m
            result.append(ok)
    elif q[0] == '2':
        T, L, R = map(int, q.split())
        result.append(st.query(L - 1, R))
print(*result, sep='\n')
