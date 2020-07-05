# エラトステネスの篩
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


X = int(input())

N = 10 ** 6
prime_table = make_prime_table(N)
for i in range(X, N + 1):
    if prime_table[i] == i:
        print(i)
        break
