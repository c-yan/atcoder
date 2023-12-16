K, X = map(int, input().split())

l = max(-1000000, X - K + 1)
r = min(1000000, X + K - 1)
print(*[i for i in range(l, r + 1)])
