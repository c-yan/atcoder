# エラトステネスの篩, 素因数分解, フェルマーの小定理
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


N = int(input())
A = list(map(int, input().split()))

m = 1000000007

prime_table = make_prime_table(10 ** 6)

lcm_factors = {}
for a in A:
    for p, e in prime_factorize(a):
        if p not in lcm_factors or lcm_factors[p] < e:
            lcm_factors[p] = e

lcm = 1
for p in lcm_factors:
    lcm *= pow(p, lcm_factors[p], m)
    lcm %= m

result = 0
for i in range(N):
    result += lcm * pow(A[i], m - 2, m)
    result %= m
print(result)
