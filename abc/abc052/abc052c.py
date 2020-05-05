from math import sqrt


def prime_factorize(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i != 0:
            continue
        t = 0
        while n % i == 0:
            n //= i
            t += 1
        result.append((i, t))
        if n == 1:
            break
    if n != 1:
        result.append((n, 1))
    return result


N = int(input())

t = [0] * (N + 1)
for i in range(2, N + 1):
    for p, c in prime_factorize(i):
        t[p] += c

result = 1
for i in range(2, N + 1):
    if t[i] == 0:
        continue
    result = result * (t[i] + 1) % 1000000007
print(result)
