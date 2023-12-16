m = 1000000007

N, *A = map(int, open(0).read().split())


def mcomb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= m
        b *= k - i
        b %= m
    return a * pow(b, -1, m)


def mhproduct(n, r):
    return mcomb(n + r - 1, r)


result = 1
prev = 0
for a in A:
    if a == -1 and prev != -1:
        start = prev
        l = 1
    elif a == -1 and prev == -1:
        l += 1
    elif a != -1 and prev == -1:
        stop = a
        result *= mhproduct(stop - start + 1, l)
        result %= m
    prev = a
print(result)
