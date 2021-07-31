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


readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

st = RangeAddSegmentTree(N)
for i in range(N):
    st.range_add(i, i + 1, A[i])

t = 0
for i in range(N - 1):
    t += abs(A[i] - A[i + 1])

result = []
for _ in range(Q):
    L, R, V = map(int, readline().split())
    L, R = L - 1, R - 1
    if L != 0:
        t -= abs(st[L - 1] - st[L])
    if R != N - 1:
        t -= abs(st[R] - st[R + 1])
    st.range_add(L, R + 1, V)
    if L != 0:
        t += abs(st[L - 1] - st[L])
    if R != N - 1:
        t += abs(st[R] - st[R + 1])
    result.append(t)
print(*result, sep='\n')
