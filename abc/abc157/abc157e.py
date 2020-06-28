# Segment tree (Bitwise Or)
from operator import or_


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

    def build(self, iterable):
        f = self._f
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = f(data[i * 2 + 1], data[i * 2 + 2])

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


def conv(c):
    return 1 << (ord(c) - ord('a'))


N = int(input())
S = input()

st = SegmentTree(N, or_)
st.build(conv(c) for c in S)

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        i, c = q[1:]
        i = int(i) - 1
        st.update(i, conv(c))
    elif q[0] == '2':
        l, r = map(int, q[1:])
        print(bin(st.query(l - 1, r)).count('1'))
