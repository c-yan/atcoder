from fractions import gcd


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
        self._data[self._offset:self._offset+self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            self._data[i] = gcd(self._data[i * 2 + 1], self._data[i * 2 + 2])

    def update(self, index, value):
        i = self._offset + index
        self._data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            self._data[i] = gcd(self._data[i * 2 + 1], self._data[i * 2 + 2])

    def query(self, start, stop):
        result = 0
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                result = gcd(result, self._data[l])
            if r & 1 == 0:
                result = gcd(result, self._data[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return result


N = int(input())
A = list(map(int, input().split()))

st = SegmentTree(N)
st.update_all(A)

result = st.query(1, N)
for i in range(1, N - 1):
    result = max(result, gcd(st.query(0, i), st.query(i + 1, N)))
result = max(result, st.query(0, N - 1))
print(result)
