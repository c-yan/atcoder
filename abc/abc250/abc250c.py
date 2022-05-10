from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())

a = list(range(N))
b = list(range(N))
for _ in range(Q):
    x = int(readline()) - 1
    i = b[x]
    if i != N - 1:
        j = i + 1
    else:
        j = i - 1
    y = a[j]
    a[i] = y
    a[j] = x
    b[x] = j
    b[y] = i
print(*[i + 1 for i in a])
