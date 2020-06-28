# Segment tree (Min)
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


N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

st = SegmentTree(N, min)
st.build(A)

result = []
i = 0
for k in range(K - 1, -1, -1):
    m = st.query(i, N - k * D)
    result.append(m)
    while A[i] != m:
        i += 1
    i += D
print(*result)
