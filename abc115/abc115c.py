N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))
