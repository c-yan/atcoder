def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
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


N, M, *A = map(int, open(0).read().split())

prime_table = make_prime_table(10 ** 5)

s = set()
for a in A:
    for p, _ in prime_factorize(a):
        s.add(p)

result = []
for k in range(1, M + 1):
    if any(p in s for p, _ in prime_factorize(k)):
        continue
    result.append(k)
print(len(result))
print(*result, sep='\n')
