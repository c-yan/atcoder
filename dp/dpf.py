# PyPy なら通る
s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        k = dp[i - 1][j]
        if dp[i][j - 1] > k:
            k = dp[i][j - 1]
        if (s[i - 1] == t[j - 1]) and (dp[i - 1][j - 1] + 1 > k):
            k = dp[i - 1][j - 1] + 1
        dp[i][j] = k
u = []
while i > 0 and j > 0:
    if dp[i - 1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j - 1] == dp[i][j]:
        j -= 1
    else:
        u.append(s[i - 1])
        i -= 1
        j -= 1
print(''.join(u[::-1]))
