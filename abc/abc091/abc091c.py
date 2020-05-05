N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

used = [False] * N
a.sort(key=lambda x: x[0], reverse=True)
b.sort(key=lambda x: x[0], reverse=True)
result = 0
for i in range(N):
    pj = -1
    miny = float('inf')
    for j in range(N):
        if used[j]:
            continue
        if a[i][0] < b[j][0] and a[i][1] < b[j][1]:
            if b[j][1] < miny:
                pj = j
                miny = b[j][1]
    if pj != -1:
        used[pj] = True
        result += 1
print(result)
