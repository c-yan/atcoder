n = int(input())
h = list(map(int, input().split()))
cost = [float('inf')] * n
cost[0] = 0
for i in range(n - 2):
    cost[i + 1] = min(cost[i + 1], cost[i] + abs(h[i + 1] - h[i]))
    cost[i + 2] = min(cost[i + 2], cost[i] + abs(h[i + 2] - h[i]))
cost[n - 1] = min(cost[n - 1], cost[n - 2] + abs(h[n - 1] - h[n - 2]))
print(cost[n - 1])
