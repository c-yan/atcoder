from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

result = []
a = [i for i in range(N)]
s = 0
for _ in range(Q):
    T, x, y = map(int, readline().split())
    if T == 1:
        i = (x - 1 + s) % N
        j = (y - 1 + s) % N
        a[i], a[j] = a[j], a[i]
    elif T == 2:
        s += N - 1
        s %= N
    elif T == 3:
        i = (x - 1 + s) % N
        result.append(A[a[i]])
print(*result, sep='\n')
