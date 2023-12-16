from itertools import accumulate

N, W = map(int, input().split())

t = [0] * (2 * 10 ** 5 + 1)

for _ in range(N):
    S, T, P = map(int, input().split())
    t[S] += P
    t[T] -= P

if all(x <= W for x in accumulate(t)):
    print('Yes')
else:
    print('No')
