N, K, M = map(int, input().split())
A = list(map(int, input().split()))

t = sum(A)
if N * M > t + K:
    print(-1)
else:
    print(max(N * M - t, 0))
