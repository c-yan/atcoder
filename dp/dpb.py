n, k = [int(e) for e in input().split()]
h = [int(e) for e in input().split()]
cost = [0] * n
for i in range(1, n):
    cost[i] = min(abs(h[i] - h[j]) + cost[j] for j in range(max(0, i - k), i))
print(cost[n - 1])
