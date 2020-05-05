N, M = map(int, input().split())

t = [0] * M
for _ in range(N):
    K, *A = map(int, input().split())
    for a in A:
        t[a - 1] += 1
print(t.count(N))
