n = int(input())
h = [int(e) for e in input().split()]
cost = [0] * n
cost[1] = abs(h[1] - h[0])
for i in range(2, n):
  cost[i] = min(abs(h[i] - h[i - 1]) + cost[i - 1], abs(h[i] - h[i - 2]) + cost[i - 2])
print(cost[n - 1])
