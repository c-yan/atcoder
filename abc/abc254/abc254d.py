N = int(input())


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


prime_table = make_prime_table(N)

result = 0
for i in range(1, N + 1):
    a = 1
    for p, e in prime_factorize(i):
        if e % 2 == 0:
            continue
        a *= p
    for c in range(1, N + 1):
        if a * c * c > N:
            break
        result += 1
print(result)
