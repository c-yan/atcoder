from sys import stdin


class RangeAddSegmentTree:
    def __init__(self, size):
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [0] * (t * 2 - 1)

    def range_add(self, start, stop, x):
        data = self._data
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                data[l] += x
            if r & 1 == 0:
                data[r - 1] += x
            l = l // 2
            r = (r - 1) // 2

    def __getitem__(self, key):
        data = self._data
        i = key + self._offset
        result = data[i]
        while i > 0:
            i = (i - 1) // 2
            result += data[i]
        return result

    def __iter__(self):
        for i in range(self._size):
            yield self[i]


readline = stdin.readline

N = int(readline())

st = RangeAddSegmentTree(24 * 60 + 1)
for _ in range(N):
    S, E = readline()[:-1].split('-')
    h = int(S[:2])
    m = int(S[2:])
    m = m // 5 * 5
    start = h * 60 + m
    h = int(E[:2])
    m = int(E[2:])
    m = (m + 4) // 5 * 5
    if m == 60:
        h += 1
        m = 0
    stop = h * 60 + m
    st.range_add(start, stop, 1)

s = -1
result = []
for i in range(24 * 60 + 1):
    if st[i] == 0 and s != -1:
        result.append('%02d%02d-%02d%02d' % (s // 60, s % 60, i // 60, i % 60))
        s = -1
    elif st[i] != 0 and s == -1:
        s = i
print(*result, sep='\n')
