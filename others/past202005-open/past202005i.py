from sys import stdin
readline = stdin.readline

N = int(readline())
Q = int(readline())

result = []
transposed = False
rows = list(range(N + 1))
cols = list(range(N + 1))
for _ in range(Q):
    Query = list(map(int, readline().split()))
    if Query[0] == 1:
        A, B = Query[1:]
        if not transposed:
            t = rows[A]
            rows[A] = rows[B]
            rows[B] = t
        else:
            t = cols[A]
            cols[A] = cols[B]
            cols[B] = t
    elif Query[0] == 2:
        A, B = Query[1:]
        if not transposed:
            t = cols[A]
            cols[A] = cols[B]
            cols[B] = t
        else:
            t = rows[A]
            rows[A] = rows[B]
            rows[B] = t
    elif Query[0] == 3:
        transposed = not transposed
    elif Query[0] == 4:
        A, B = Query[1:]
        y, x = A, B
        if transposed:
            y, x = x, y
        y = rows[y]
        x = cols[x]
        result.append(N * (y - 1) + x - 1)
print('\n'.join(str(i) for i in result))
