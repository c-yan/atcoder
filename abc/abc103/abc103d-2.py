# Segment tree (Sum)
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
        self._data = [0 for _ in range(t * 2 - 1)]

    def update(self, index, value):
        i = self._offset + index
        self._data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            self._data[i] = self._data[i * 2 + 1] + self._data[i * 2 + 2]

    def query(self, start, stop):
        result = 0
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                result = result + self._data[l]
            if r & 1 == 0:
                result = result + self._data[r - 1]
            l = l // 2
            r = (r - 1) // 2
        return result


N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])
st = SegmentTree(N - 1)

result = 0
for a, b in ab:
    a, b = a - 1, b - 1
    if st.query(a, b) != 0:
        continue
    result += 1
    st.update(b - 1, 1)
print(result)
