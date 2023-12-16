from sys import stdin
from bisect import bisect_left


class RangeUpdateSegmentTree:
    def __init__(self, size):
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [(-1, 0)] * (t * 2 - 1)
        self._counter = 0

    def range_update(self, start, stop, x):
        data = self._data
        counter = self._counter
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                data[l] = (counter, x)
            if r & 1 == 0:
                data[r - 1] = (counter, x)
            l = l // 2
            r = (r - 1) // 2
        self._counter += 1

    def __getitem__(self, key):
        data = self._data
        i = key + self._offset
        t = data[i]
        while i > 0:
            i = (i - 1) // 2
            t = max(t, data[i])
        return t[1]

    def __iter__(self):
        for i in range(self._size):
            yield self[i]


readline = stdin.readline

N, Q = map(int, readline().split())
STX = [tuple(map(int, readline().split())) for _ in range(N)]
D = [int(readline()) for _ in range(Q)]

STX.sort(key=lambda x: x[2], reverse=True)

st = RangeUpdateSegmentTree(Q)
st.range_update(0, Q, -1)
for S, T, X in STX:
    st.range_update(bisect_left(D, S - X), bisect_left(D, T - X), X)
print(*st, sep='\n')
