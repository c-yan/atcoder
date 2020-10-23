N, K = map(int, input().split())

a = 3 * 2 * (K - 1) * (N - K)  # count(K) == 1
b = 3 * (N - 1)                # count(K) == 2
c = 1                          # count(K) == 3
print((a + b + c) / (N * N * N))
