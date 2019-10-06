# DP(配るDP)
N = int(input())
a = list(map(int, input().split()))

t = [float('inf')] * N
t[0] = 0
for i in range(N - 2):
    t[i + 1] = min(t[i + 1], t[i] + abs(a[i + 1] - a[i]))
    t[i + 2] = min(t[i + 2], t[i] + abs(a[i + 2] - a[i]))
t[N - 1] = min(t[N - 1], t[N - 2] + abs(a[N - 1] - a[N - 2]))
print(t[N - 1])
