# 貰うDP
INF = float('inf')
n = int(input())
a = [1]
i = 6
while i <= n:
    a.append(i)
    i *= 6
i = 9
while i <= n:
    a.append(i)
    i *= 9
t = [0] * (n + 1)
for i in range(1, n + 1):
    k = INF
    for j in a:
        if i - j >= 0 and k > t[i - j] + 1:
            k = t[i - j] + 1
    t[i] = k
print(t[n])
