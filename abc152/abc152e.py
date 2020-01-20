def mpow(x, n):
    result = 1
    while n != 0:
        if n & 1 == 1:
            result *= x
            result %= 1000000007
        x *= x
        x %= 1000000007
        n >>= 1
    return result


max_A = 1000000

N = int(input())
A = list(map(int, input().split()))

sieve = [0] * (max_A + 1)
sieve[0] = -1
sieve[1] = -1
for i in range(2, max_A + 1):
    if sieve[i] != 0:
        continue
    sieve[i] = i
    for j in range(i * i, max_A + 1, i):
        if sieve[j] == 0:
            sieve[j] = i

lcm_factors = {}
for i in range(N):
    t = []
    a = A[i]
    while a != 1:
        if len(t) == 0:
            t.append([sieve[a], 1])
        elif t[-1][0] == sieve[a]:
            t[-1][1] += 1
        else:
            t.append([sieve[a], 1])
        a //= sieve[a]
    for k, v in t:
        if k not in lcm_factors or lcm_factors[k] < v:
            lcm_factors[k] = v

lcm = 1
for k in lcm_factors:
    for i in range(lcm_factors[k]):
        lcm *= k
        lcm %= 1000000007

result = 0
for i in range(N):
    result += lcm * mpow(A[i], 1000000007-2)
    result %= 1000000007
print(result)
