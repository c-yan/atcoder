from sys import stdin

readline = stdin.readline

N = int(readline())
tlr = [map(int, readline().split()) for _ in range(N)]

lr = []
for t, l, r in tlr:
    if t == 1:
        lr.append((l, r))
    elif t == 2:
        lr.append((l, r - 0.1))
    elif t == 3:
        lr.append((l + 0.1, r))
    elif t == 4:
        lr.append((l + 0.1, r - 0.1))

result = 0
for i in range(N):
    for j in range(i + 1, N):
        a, b = lr[i]
        c, d = lr[j]
        if c > b or d < a:
            continue
        result += 1
print(result)
