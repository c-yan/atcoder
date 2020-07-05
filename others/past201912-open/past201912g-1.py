N = int(input())
a = [list(map(int, input().split())) for _ in range(N - 1)]

result = -float('inf')
t = [0] * N
for _ in range(3 ** N):
    s = 0
    for i in range(N):
        for j in range(i + 1, N):
            if t[i] == t[j]:
                s += a[i][j - i - 1]
    result = max(result, s)
    for i in range(N):
        if t[i] < 2:
            t[i] += 1
            break
        t[i] = 0
print(result)
