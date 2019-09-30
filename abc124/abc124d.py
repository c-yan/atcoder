# しゃくとり法
N, K = map(int, input().split())
S = list(map(int, input()))

j = 1
r = 0
t = []
for i in range(N):
    if S[i] == j:
        r += 1
    else:
        t.append(r)
        r = 1
        j ^= 1
t.append(r)
if j == 0:
    t.append(0)

if K >= (len(t) - 1) // 2:
    print(sum(t))
else:
    result = sum(t[:2 * K + 1])
    j = result
    i = 2
    while i + 2 * K < len(t):
        j += t[i + 2 * K - 1] + t[i + 2 * K] - (t[i - 2] + t[i - 1])
        result = max(result, j)
        i += 2
    print(result)
