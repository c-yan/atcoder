def scan(s):
    m = 0
    a = 0
    for c in s:
        if c == '(':
            a += 1
        elif c == ')':
            a -= 1
        m = min(m, a)
    return m, a


def custom_key(v):
    m, a = v
    if a >= 0:
        return 1, m, a
    else:
        return -1, a - m, a


N = int(input())
S = [input() for _ in range(N)]

c = 0
for m, a in sorted([scan(s) for s in S], reverse=True, key=custom_key):
    if c + m < 0:
        c += m
        break
    c += a

if c == 0:
    print('Yes')
else:
    print('No')
