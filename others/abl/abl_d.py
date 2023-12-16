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


max_A = 300000

N, K, *A = map(int, open(0).read().split())

st = SegmentTree(max_A + 1, max, 0)
for a in A:
    st[a] = st.query(max(a - K, 0), min(a + K + 1, max_A + 1)) + 1

print(st.query(0, max_A + 1))
