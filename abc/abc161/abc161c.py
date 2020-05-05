N, K = map(int, input().split())

x = N % K
print(min(x, K - x))
