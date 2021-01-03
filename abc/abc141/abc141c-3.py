from sys import stdin


class RangeAddSegmentTree:
    def __init__(self, size):
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [0] * (t * 2 - 1)

    def add(self, start, stop, x):
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

    def get(self, i):
        data = self._data
        j = i + self._offset
        result = data[j]
        while j > 0:
            j = (j - 1) // 2
            result += data[j]
        return result


N, K, Q, *A = map(int, open(0).read().split())

st = RangeAddSegmentTree(N)
st.add(0, N, K)
for a in A:
    st.add(0, a - 1, -1)
    st.add(a, N, -1)

result = []
for i in range(N):
    if st.get(i) > 0:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
