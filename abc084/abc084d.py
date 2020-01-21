# エラトステネスの篩, 累積和
from math import sqrt

max_lr = 10 ** 5

sieve = [True] * (max_lr + 1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(sqrt(max_lr)) + 1):
    if not sieve[i]:
        continue
    for j in range(i * i, max_lr + 1, i):
        sieve[j] = False

cs = [0] * (max_lr + 1)
for i in range(3, max_lr + 1, 2):
    if sieve[i] and sieve[(i + 1) // 2]:
        cs[i] = 1
for i in range(1, max_lr + 1):
    cs[i] += cs[i - 1]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(cs[r] - cs[l - 1])
