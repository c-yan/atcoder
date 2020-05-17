from math import gcd

N = int(input())
AB = [map(int, input().split()) for _ in range(N)]

t = []
d = {}
d[0] = {}
d[0][0] = 0
for a, b in AB:
    i = gcd(a, b)
    if i != 0:
        a //= i
        b //= i
    t.append((a, b))
    d.setdefault(a, {})
    d[a].setdefault(b, 0)
    d[a][b] += 1

used = set()
result = 1
for a, b in t:
    if (a, b) in used:
        continue
    used.add((a, b))
    if a == 0 and b == 0:
        continue
    i = d[a][b]
    j, k, l = 0, 0, 0
    if -a in d and -b in d[-a]:
        j = d[-a][-b]
        used.add((-a, -b))
    if -b in d and a in d[-b]:
        k = d[-b][a]
        used.add((-b, a))
    if b in d and -a in d[b]:
        l = d[b][-a]
        used.add((b, -a))
    result *= pow(2, i + j, 1000000007) + pow(2, k + l, 1000000007) - 1
    result %= 1000000007
result += d[0][0] - 1
result %= 1000000007
print(result)
