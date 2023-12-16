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

L, Q = map(int, readline().split())
cx = [tuple(map(int, readline().split())) for _ in range(Q)]

a = sorted([x for _, x in cx] + [0, L])
b = {}
for i in range(len(a)):
    b[a[i]] = i

st1 = SegmentTree(len(a), max, -1)
st2 = SegmentTree(len(a), min, 10 ** 20)
st1[b[0]] = b[0]
st1[b[L]] = b[L]
st2[b[0]] = b[0]
st2[b[L]] = b[L]

result = []
for c, x in cx:
    if c == 1:
        st1[b[x]] = b[x]
        st2[b[x]] = b[x]
    elif c == 2:
        result.append(a[st2.query(b[x], b[L] + 1)] - a[st1.query(0, b[x])])
print(*result, sep='\n')
