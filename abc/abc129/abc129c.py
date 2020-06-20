# DP(動的計画法)
N, M = map(int, input().split())
A = set(int(input()) for _ in range(M))

m = 1000000007

t = [0] * (N + 2)
t[0] = 1
for i in range(N):
    if i in A:
        t[i] = 0
    else:
        t[i + 1] = (t[i + 1] + t[i]) % m
        t[i + 2] = (t[i + 2] + t[i]) % m
print(t[N])
