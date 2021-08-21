m = 998244353

N = int(input())
S = input()


def conv(current, used):
    return current + (used << 5)


def deconv(x):
    return x & 31, x >> 5


a = {conv(0, 0): 1}
for x in [ord(c) - ord('A') + 1 for c in S]:
    b = {}
    for y in a:
        c, u = deconv(y)
        if c == x:
            b.setdefault(y, 0)
            b[y] += a[y]
            b[y] %= m
        elif u & (1 << x) == 0:
            t = conv(x, u + (1 << x))
            b.setdefault(t, 0)
            b[t] += a[y]
            b[t] %= m
        b.setdefault(y, 0)
        b[y] += a[y]
        b[y] %= m
    a = b

result = 0
for k in a:
    if k == conv(0, 0):
        continue
    result += a[k]
    result %= m
print(result)
