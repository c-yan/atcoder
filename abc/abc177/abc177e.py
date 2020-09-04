from math import gcd
from functools import reduce


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


def is_pairwise_coprime():
    s = set()
    for i in range(N - 1, -1, -1):
        t = prime_factorize(A[i])
        for p, _ in t:
            if p in s:
                return False
            s.add(p)
    return True


N, *A = map(int, open(0).read().split())

prime_table = make_prime_table(10 ** 6)
if is_pairwise_coprime():
    print('pairwise coprime')
elif reduce(gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')
