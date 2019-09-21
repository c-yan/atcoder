# DP(動的計画法)
n, m = [int(e) for e in input().split()]
a = set(int(input()) for i in range(m))
t = [0] * (n + 2)
t[0] = 1
for i in range(n):
    if i in a:
        t[i] = 0
    else:
        t[i + 1] = (t[i + 1] + t[i]) % 1000000007
        t[i + 2] = (t[i + 2] + t[i]) % 1000000007
print(t[n])
