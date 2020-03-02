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

    def update_all(self, iterable):
        self._data[self._offset:self._offset+self._size] = [1 << (ord(c) - ord('a')) for c in iterable]
        for i in range(self._offset - 1, -1, -1):
            self._data[i] = self._data[i * 2 + 1] | self._data[i * 2 + 2]

    def update(self, index, value):
        i = self._offset + index
        self._data[i] = 1 << (ord(value) - ord('a'))
        while i >= 1:
            i = (i - 1) // 2
            self._data[i] = self._data[i * 2 + 1] | self._data[i * 2 + 2]

    def query(self, start, stop):
        result = 0
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                result = result | self._data[l]
            if r & 1 == 0:
                result = result | self._data[r - 1]
            l = l // 2
            r = (r - 1) // 2
        return result


N = int(input())
S = input()

st = SegmentTree(N)
st.update_all(S)

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        i, c = q[1:]
        i = int(i) - 1
        st.update(i, c)
    elif q[0] == '2':
        l, r = map(int, q[1:])
        print(bin(st.query(l - 1, r)).count('1'))
