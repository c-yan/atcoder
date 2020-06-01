from fractions import gcd


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


A, B = map(int, input().split())

print(len(prime_factorize(gcd(A, B))) + 1)
