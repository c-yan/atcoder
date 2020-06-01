def prime_factorize(n):
    result = []
    if n % 2 == 0:
        t = 0
        while n % 2 == 0:
            n //= 2
            t += 1
        result.append((2, t))
    for i in range(3, int(n ** 0.5) + 1, 2):
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
    for p, e in prime_factorize(i):
        t[p] += e

result = 1
for i in range(2, N + 1):
    if t[i] == 0:
        continue
    result = result * (t[i] + 1) % 1000000007
print(result)
