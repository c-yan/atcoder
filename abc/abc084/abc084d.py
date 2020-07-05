# エラトステネスの篩, 累積和
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


max_lr = 10 ** 5

prime_table = make_prime_table(max_lr)

cs = [0] * (max_lr + 1)
for i in range(3, max_lr + 1, 2):
    j = (i + 1) // 2
    if prime_table[i] == i and prime_table[j] == j:
        cs[i] = 1
for i in range(1, max_lr + 1):
    cs[i] += cs[i - 1]

Q = int(input())
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(cs[r] - cs[l - 1])
print('\n'.join(str(i) for i in result))
