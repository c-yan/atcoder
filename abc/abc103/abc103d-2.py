# Segment tree (+)
from operator import add
from sys import stdin


class SegmentTree:
    _f = None
    _size = None
    _offset = None
    _data = None

    def __init__(self, size, f):
        self._f = f
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [0] * (t * 2 - 1)

    def update(self, index, value):
        f = self._f
        data = self._data
        i = self._offset + index
        data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            data[i] = f(data[i * 2 + 1], data[i * 2 + 2])

    def query(self, start, stop):
        def iter_segments(data, l, r):
            while l < r:
                if l & 1 == 0:
                    yield data[l]
                if r & 1 == 0:
                    yield data[r - 1]
                l = l // 2
                r = (r - 1) // 2
        f = self._f
        it = iter_segments(self._data, start + self._offset,
                           stop + self._offset)
        result = next(it)
        for e in it:
            result = f(result, e)
        return result


readline = stdin.readline

N, M = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])
st = SegmentTree(N - 1, add)

result = 0
for a, b in ab:
    a, b = a - 1, b - 1
    if st.query(a, b) != 0:
        continue
    result += 1
    st.update(b - 1, 1)
print(result)
