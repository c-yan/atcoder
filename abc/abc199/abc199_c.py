from sys import stdin

readline = stdin.readline

N = int(readline())
S = readline()[:-1]
Q = int(readline())

t = list(S)
flipped = False
for _ in range(Q):
    T, A, B = map(int, readline().split())
    if T == 1:
        a = A - 1
        b = B - 1
        if flipped:
            a = (a + N) % (2 * N)
            b = (b + N) % (2 * N)
        t[a], t[b] = t[b], t[a]
    elif T == 2:
        flipped = not flipped

if flipped:
    print(''.join(t[N:] + t[:N]))
else:
    print(''.join(t))
