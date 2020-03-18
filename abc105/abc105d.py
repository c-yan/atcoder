N, M = map(int, input().split())
A = list(map(int, input().split()))

t = {}
c = 0
for a in A:
    c += a
    c %= M
    if c in t:
        t[c] += 1
    else:
        t[c] = 1

result = 0
if 0 in t:
    result += t[0]
c = 0
for a in A:
    c += a
    c %= M
    t[c] -= 1
    result += t[c]
print(result)
