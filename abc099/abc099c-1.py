# 配るDP
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
t = [float('inf')] * (n + 1)
t[0] = 0
for i in range(n):
  for j in a:
    if i + j <= n and t[i + j] > t[i] + 1:
      t[i + j] = t[i] + 1
print(t[n])
