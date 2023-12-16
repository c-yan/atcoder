A, B, K = map(int, input().split())


def comb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        b *= k - i
    return a // b


def h(n, k):
    return comb(n + k - 1, k)


n = 0
result = ''
a, b = A, B
while a != 0 and b != 0:
    t = h(b + 1, a - 1)
    if n + t >= K:
        result += 'a'
        a -= 1
    else:
        result += 'b'
        b -= 1
        n += t
result += 'a' * a + 'b' * b
print(result)
