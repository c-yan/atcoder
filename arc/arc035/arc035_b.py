from collections import Counter

m = 1000000007


def make_factorial_table(n):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i - 1] * i % m
    return result


N, *T = map(int, open(0).read().split())

ft = make_factorial_table(N)

c = Counter(T)
a = 0
b = 1
t = 0
for k in sorted(c):
    for _ in range(c[k]):
        t += k
        a += t
    b *= ft[c[k]]
    b %= m
print(a)
print(b)
