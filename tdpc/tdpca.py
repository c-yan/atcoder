N = int(input())
p = list(map(int, input().split()))
t = [0] * (10001)
t[0] = 1
for i in range(N):
  for j in range(10000, -1, -1):
    if t[j] == 0:
      continue
    t[j + p[i]] = 1
print(sum(t))
