def encode_runlength(s):
    result = []
    p = s[0]
    a = 1
    for c in s[1:]:
        if p == c:
            a += 1
            continue
        result.append((p, a))
        p = c
        a = 1
    result.append((p, a))
    return result


S = input()
T = input()

s = encode_runlength(S)
t = encode_runlength(T)

if len(s) != len(t):
    print('No')
    exit()

for (c0, a0), (c1, a1) in zip(s, t):
    if c0 != c1:
        print('No')
        exit()
    if a0 >= 2 and a1 > a0:
        a0 = a1
    if a0 != a1:
        print('No')
        exit()
print('Yes')
