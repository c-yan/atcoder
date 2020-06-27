# エラトステネスの篩
N = int(input())

sieve = [0] * (N + 1)
sieve[0] = -1
sieve[1] = -1
for i in range(2, N + 1):
    if sieve[i] != 0:
        continue
    sieve[i] = i
    for j in range(i * i, N + 1, i):
        if sieve[j] == 0:
            sieve[j] = i


def f(X):
    t = []
    a = X
    while a != 1:
        if len(t) != 0 and t[-1][0] == sieve[a]:
            t[-1][1] += 1
        else:
            t.append([sieve[a], 1])
        a //= sieve[a]
    result = 1
    for _, n in t:
        result *= n + 1
    return result


result = 0
for K in range(1, N + 1):
    result += K * f(K)
print(result)
