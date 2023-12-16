def is_ok(s):
    if s[1:] in ['AGC', 'ACG', 'GAC']:
        return False
    if s[0] == 'A' and s[2:] == 'GC':
        return False
    if s[:2] == 'AG' and s[3] == 'C':
        return False
    return True


m = 1000000007

N = int(input())

d = {}
for i in 'ACGT':
    for j in 'ACGT':
        for k in 'ACGT':
            d[i + j + k] = 1
for k in ['AGC', 'ACG', 'GAC']:
    del d[k]

for i in range(N - 3):
    t = {}
    for k in d:
        for i in 'ACGT':
            s = k + i
            if is_ok(s):
                t.setdefault(s[1:], 0)
                t[s[1:]] += d[k]
                t[s[1:]] %= m
    d = t

print(sum(d.values()) % m)
