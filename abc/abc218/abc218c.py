N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


def trim(a):
    while a[0] == '.' * len(a[0]):
        a = a[1:]
    while a[-1] == '.' * len(a[-1]):
        a = a[:-1]
    return a


def rotate(a):
    r = ['' for _ in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a) - 1, -1, -1):
            r[i] += a[j][i]
    return r


S = trim(S)
T = trim(T)
S = rotate(S)
T = rotate(T)
S = trim(S)
T = trim(T)

for i in range(4):
    T = rotate(T)
    if len(S) != len(T):
        continue
    if any(S[i] != T[i] for i in range(len(S))):
        continue
    print('Yes')
    break
else:
    print('No')
