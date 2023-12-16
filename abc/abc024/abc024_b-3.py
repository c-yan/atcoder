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


N, T, *A = map(int, open(0).read().split())

st = RangeAddSegmentTree(10 ** 6 + T)
for a in A:
    st.range_add(a, a + T, 1)
print(10 ** 6 + T - list(st).count(0))
