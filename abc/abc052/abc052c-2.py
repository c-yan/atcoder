# エラトステネスの篩, 素因数分解
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result


N = int(input())

m = 1000000007

prime_table = make_prime_table(N)

t = [0] * (N + 1)
for i in range(2, N + 1):
    for p, e in prime_factorize(i):
        t[p] += e

result = 1
for i in range(2, N + 1):
    if t[i] == 0:
        continue
    result = result * (t[i] + 1) % m
print(result)
