def conv(s):
    if s.find('.') == -1:
        s += '.'
    s = s.rstrip('0')
    t = len(s) - s.find('.') - 1
    a = int(s.replace('.', ''))
    if a == 0:
        return (0, 0)
    x, y = -t, -t
    while a % 5 == 0:
        x += 1
        a //= 5
    while a % 2 == 0:
        y += 1
        a //= 2
    return (x, y)


N, *A = open(0).read().split()
N = int(N)

d = {}
for a in A:
    t = conv(a)
    d.setdefault(t, 0)
    d[t] += 1

result = 0
xs = list(d)
for i in range(len(xs)):
    x, y = xs[i]
    t = d[xs[i]]
    if x >= 0 and y >= 0:
        result += t * (t - 1) // 2
    for j in range(i + 1, len(xs)):
        m, n = xs[j]
        if x + m >= 0 and y + n >= 0:
            result += t * d[xs[j]]
print(result)
