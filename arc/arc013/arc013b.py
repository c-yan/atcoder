C = int(input())

t = [0, 0, 0]
for _ in range(C):
    N, M, L = map(int, input().split())
    a = sorted([N, M, L])
    for i in range(3):
        t[i] = max(t[i], a[i])
print(t[0] * t[1] * t[2])
