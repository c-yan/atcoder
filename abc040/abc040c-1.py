# DP(貰うDP)
N = int(input())
a = list(map(int, input().split()))

t = [0] * N
t[1] = t[0] + abs(a[1] - a[0])
for i in range(2, N):
    t[i] = min(t[i - 1] + abs(a[i] - a[i - 1]),
               t[i - 2] + abs(a[i] - a[i - 2]))
print(t[N - 1])
