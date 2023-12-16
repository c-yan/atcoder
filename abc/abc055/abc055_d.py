from itertools import product

N = int(input())
s = input()

swap = {'S': 'W', 'W': 'S'}
for a, b in product('SW', repeat=2):
    t = [None] * N
    t[0] = a
    t[1] = b
    for i in range(1, N - 1):
        if t[i] == 'S':
            if s[i] == 'o':
                t[i + 1] = t[i - 1]
            elif s[i] == 'x':
                t[i + 1] = swap[t[i - 1]]
        elif t[i] == 'W':
            if s[i] == 'o':
                t[i + 1] = swap[t[i - 1]]
            elif s[i] == 'x':
                t[i + 1] = t[i - 1]
    if t[N - 1] == 'S':
        if s[N - 1] == 'o' and t[N - 2] != t[0]:
            continue
        elif s[N - 1] == 'x' and t[N - 2] == t[0]:
            continue
    elif t[N - 1] == 'W':
        if s[N - 1] == 'o' and t[N - 2] == t[0]:
            continue
        elif s[N - 1] == 'x' and t[N - 2] != t[0]:
            continue
    if t[0] == 'S':
        if s[0] == 'o' and t[N - 1] != t[1]:
            continue
        elif s[0] == 'x' and t[N - 1] == t[1]:
            continue
    elif t[0] == 'W':
        if s[0] == 'o' and t[N - 1] == t[1]:
            continue
        elif s[0] == 'x' and t[N - 1] != t[1]:
            continue
    print(''.join(t))
    exit()
print(-1)
