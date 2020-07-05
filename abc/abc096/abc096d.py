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


N = int(input())

result = []
prime_table = make_prime_table(55555)
for i in range(3, 55555 + 1, 2):
    if prime_table[i] == i and i % 5 == 1:
        result.append(i)
    if len(result) == N:
        break
print(*result)
