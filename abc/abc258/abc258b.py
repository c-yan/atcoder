N = int(input())
A = [list(map(int, input())) for _ in range(N)]

result = 0
for y in range(N):
    for x in range(N):
        t = 0
        for i in range(N):
            t = t * 10 + A[(y - i + N) % N][x]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[(y - i + N) % N][(x + i) % N]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[y][(x + i) % N]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[(y + i) % N][(x + i) % N]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[(y + i) % N][x]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[(y + i) % N][(x - i + N) % N]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[y][(x - i + N) % N]
        result = max(result, t)

        t = 0
        for i in range(N):
            t = t * 10 + A[(y - i + N) % N][(x - i + N) % N]
        result = max(result, t)
print(result)
