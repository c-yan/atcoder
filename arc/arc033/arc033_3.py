from sys import stdin
from operator import add


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

Q = int(readline())

st = SegmentTree(200000, add, 0)
result = []
for _ in range(Q):
    T, X = map(int, readline().split())
    if T == 1:
        st[X - 1] += 1
    elif T == 2:
        ok = 200000
        ng = 0
        while ok - ng > 1:
            m = ng + (ok - ng) // 2
            if st.query(0, m) >= X:
                ok = m
            else:
                ng = m
        result.append(ok)
        st[ok - 1] -= 1
if len(result) != 0:
    print(*result, sep='\n')
