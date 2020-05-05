class SegmentTree():
    _data = []
    _offset = 0
    _size = 0

    def __init__(self, size):
        _size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [0] * (t * 2 - 1)

    def update_all(self, iterable):
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = min(data[i * 2 + 1], data[i * 2 + 2])

    def update(self, index, value):
        data = self._data
        i = self._offset + index
        data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            data[i] = min(data[i * 2 + 1], data[i * 2 + 2])

    def query(self, start, stop):
        data = self._data
        result = float('inf')
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                result = min(result, data[l])
            if r & 1 == 0:
                result = min(result, data[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return result


N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

st = SegmentTree(N)
st.update_all(A)

result = []
i = 0
for k in range(K - 1, -1, -1):
    m = st.query(i, N - k * D)
    result.append(m)
    while A[i] != m:
        i += 1
    i += D
print(*result)
