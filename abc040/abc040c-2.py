# 配るDP
n = int(input())
a = list(map(int, input().split()))
t = [float('inf')] * n
t[0] = 0
for i in range(n - 2):
    t[i + 1] = min(t[i + 1], t[i] + abs(a[i + 1] - a[i]))
    t[i + 2] = min(t[i + 2], t[i] + abs(a[i + 2] - a[i]))
t[n - 1] = min(t[n - 1], t[n - 2] + abs(a[n - 1] - a[n - 2]))
print(t[n - 1])
