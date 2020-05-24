N = int(input())

result = []
sieve = [0] * (55555  + 1)
sieve[0] = -1
sieve[1] = -1
for i in range(2, 55555 + 1):
    if sieve[i] != 0:
        continue
    if i % 5 == 1:
        result.append(i)
        if len(result) == N:
            break
    sieve[i] = i
    for j in range(i * i, 55555 + 1, i):
        if sieve[j] == 0:
            sieve[j] = i
print(*result)
