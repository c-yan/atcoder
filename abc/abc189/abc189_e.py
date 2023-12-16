from sys import stdin

readline = stdin.readline

N = int(readline())
XY = [tuple(map(int, readline().split())) for _ in range(N)]
M = int(readline())
op = [readline() for _ in range(M)]
Q = int(readline())
AB = [tuple(map(int, readline().split())) for _ in range(Q)]

# (x, y)
# 1 -> (y, -x)
# 2 -> (-y, x)
# 3 p -> (2p - x, y)
# 4 p -> (x, 2p - y)


def e(x, i):
    result = x[0]
    if x[1] == 1:
        result += XY[i][x[2]]
    elif x[1] == -1:
        result -= XY[i][x[2]]
    return result


x = (0, 1, 0)
y = (0, 1, 1)
applied = 0
result = [None] * Q
for a, b, i in sorted(((AB[i][0], AB[i][1], i) for i in range(Q)), key=lambda x: x[0]):
    while applied < a:
        o = op[applied]
        if o[0] == '1':
            t = x
            x = (y[0], y[1], y[2])
            y = (-t[0], -t[1], t[2])
        if o[0] == '2':
            t = x
            x = (-y[0], -y[1], y[2])
            y = (t[0], t[1], t[2])
        if o[0] == '3':
            p = int(o[2:])
            x = (2 * p - x[0], -x[1], x[2])
        if o[0] == '4':
            p = int(o[2:])
            y = (2 * p - y[0], -y[1], y[2])
        applied += 1
    result[i] = '%d %d' % (e(x, b - 1), e(y, (b - 1)))
print(*result, sep='\n')
