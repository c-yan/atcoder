def enumerate_divisors(n):
    t = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        yield i
        if i * i != n:
            t.append(n // i)
    yield from reversed(t)


N = int(input())

a = N
while a % 2 == 0:
    a //= 2

print(2 * len(list(enumerate_divisors(a))))
