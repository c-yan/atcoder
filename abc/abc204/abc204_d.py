N, *T = map(int, open(0).read().split())

c = sum(T)
dp = [0] * (c + 1)
dp[0] = 1
for t in T:
    for i in range(c, -1, -1):
        if dp[i] == 0:
            continue
        dp[i + t] = 1

result = c
for i in range(c + 1):
    if dp[i] == 0:
        continue
    result = min(result, max(i, c - i))
print(result)
