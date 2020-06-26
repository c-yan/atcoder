# Segment tree (Min)
class SegmentTree():
    _data = None
    _index = None
    _offset = None

    def __init__(self, data):
        size = len(data)
        t = 1
        while t < size:
            t <<= 1
        offset = t - 1
        index = [0] * (t * 2 - 1)
        index[offset:offset + size] = range(size)
        for i in range(offset - 1, -1, -1):
            x = index[i * 2 + 1]
            y = index[i * 2 + 2]
            if data[x] <= data[y]:
                index[i] = x
            else:
                index[i] = y
        self._data = data
        self._index = index
        self._offset = offset

    def query(self, start, stop):
        data = self._data
        index = self._index
        result = start
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                i = index[l]
                x = data[i]
                y = data[result]
                if x < y or (x == y and i < result):
                    result = i
            if r & 1 == 0:
                i = index[r - 1]
                x = data[i]
                y = data[result]
                if x < y or (x == y and i < result):
                    result = i
            l = l // 2
            r = (r - 1) // 2
        return result


N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

st = SegmentTree(A)

result = []
i = 0
for k in range(K - 1, -1, -1):
    i = st.query(i, N - k * D)
    result.append(A[i])
    i += D
print(*result)
