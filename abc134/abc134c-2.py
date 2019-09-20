# 累積和(max)
N = int(input())
a = [int(input()) for _ in range(N)]
lam = a[:]
ram = a[:]
for i in range(1, N):
  lam[i] = max(lam[i], lam[i - 1])
for i in range(N - 2, -1, -1):
  ram[i] = max(ram[i], ram[i + 1])
print(ram[1])
for i in range(1, N - 1):
  print(max(lam[i - 1], ram[i + 1]))
print(lam[N - 2])
