def make_factorial_table(n):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i - 1] * i % m
    return result


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


m = 1000000007

S = int(input())

fac = make_factorial_table(S + 10)

result = 0
for i in range(1, S // 3 + 1):
    result += mcomb(S - i * 3 + i - 1, i - 1)
    result %= m
print(result)
