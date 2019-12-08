N = int(input())

s = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        s[i].append((x - 1, y))

result = 0
for i in range(1, 2 ** N):
    t = [-1] * N
    for j in range(N):
        t[j] = (i >> j) & 1
    m = False
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        for x, y in s[j]:
            if t[x] != y:
                m = True
                break
    if not m:
        result = max(result, bin(i)[2:].count('1'))
print(result)
