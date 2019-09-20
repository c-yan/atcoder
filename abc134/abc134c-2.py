# 累積和(max)
N = int(input())
a = [int(input()) for _ in range(N)]
lcm = a[:]
rcm = a[:]
for i in range(1, N):
  lcm[i] = max(lcm[i], lcm[i - 1])
for i in range(N - 2, -1, -1):
  rcm[i] = max(rcm[i], rcm[i + 1])
print(rcm[1])
for i in range(1, N - 1):
  print(max(lcm[i - 1], rcm[i + 1]))
print(lcm[N - 2])
