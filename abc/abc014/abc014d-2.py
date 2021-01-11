from sys import setrecursionlimit, stdin


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

    def __iter__(self):
        for i in range(self._size):
            yield self[i]

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


setrecursionlimit(10 ** 6)
readline = stdin.readline

N = int(readline())
links = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda x: int(x) - 1, readline().split())
    links[x].append(y)
    links[y].append(x)

depth = [-1] * N
vs = []


def do_euler_tour(n, d):
    depth[n] = d
    for c in links[n]:
        if depth[c] != -1:
            continue
        vs.append(n)
        do_euler_tour(c, d + 1)
    vs.append(n)


do_euler_tour(0, 0)

left = [-1] * N
for i in range(len(vs)):
    if left[vs[i]] != -1:
        continue
    left[vs[i]] = i

st = SegmentTree(len(vs), min, (10 ** 18, 0))
st.build((depth[vs[i]], i) for i in range(len(vs)))


# get_lowest_common_ancestor
def get_lca(a, b):
    x, y = left[a], left[b]
    if x > y:
        x, y = y, x
    return vs[st.query(x, y + 1)[1]]


result = []
Q = int(readline())
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, readline().split())
    c = get_lca(a, b)
    result.append(depth[a] + depth[b] - 2 * depth[c] + 1)
print(*result, sep='\n')
