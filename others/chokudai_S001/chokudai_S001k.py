def bit_add(bit, i, x):
    i += 1
    n = len(bit)
    while i <= n:
        bit[i - 1] += x
        i += i & -i


def bit_sum(bit, i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i - 1]
        i -= i & -i
    return result


def bit_query(bit, start, stop):
    return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


N, *a = map(int, open(0).read().split())

m = 1000000007

fac = [0] * (N + 1)
fac[0] = 1
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i
    fac[i] %= m

bit = [0] * (N + 1)
result = 1
for x in a:
    result += (x - 1 - bit_query(bit, 1, x)) * fac[N - 1 - bit_query(bit, 1, N + 1)]
    result %= m
    bit_add(bit, x, 1)
print(result)
