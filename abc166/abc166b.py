N, K = map(int, input().split())

t = [0] * N
for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        t[a - 1] += 1
print(t.count(0))
