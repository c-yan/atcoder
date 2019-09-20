# 累積和(max)
N = int(input())
a = [int(input()) for _ in range(N)]
lam = [0] * N
ram = [0] * N
lam[0] = a[0]
ram[N - 1] = a[N - 1]
for i in range(1, N):
  lam[i] = max(lam[i - 1], a[i])
  ram[N - 1 - i] = max(ram[N - 1 - i + 1], a[N - 1 - i])
print(ram[1])
for i in range(1, N - 1):
  print(max(lam[i - 1], ram[i + 1]))
print(lam[N - 2])
