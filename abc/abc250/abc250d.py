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

prime_table = make_prime_table(10 ** 6)
primes = [i for i in range(10 ** 6 + 1) if prime_table[i] == i]

result = 0
l = 0
for r in range(len(primes) - 1, 0, -1):
    while primes[l] * (primes[r] ** 3) <= N and l < r:
        l += 1
    result += l
    if l == r:
        l -= 1
print(result)
