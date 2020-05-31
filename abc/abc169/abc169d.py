from math import sqrt

N = int(input())

rn = int(sqrt(N))
sieve = [0] * (rn + 1)
sieve[0] = -1
sieve[1] = -1
t = [0] * (rn + 1)
for i in range(2, rn + 1):
    if sieve[i] != 0:
        continue
    sieve[i] = i
    j = i
    while j < rn + 1:
        t[j] = 1
        j *= i
    for j in range(i * i, rn + 1, i):
        if sieve[j] == 0:
            sieve[j] = i

result = 0
last = -1
for i in range(2, rn + 1):
    if t[i] == 0:
        continue
    if N % i == 0:
        result += 1
        N //= i
        last = i
if N != 1 and N > rn:
    result += 1
print(result)
