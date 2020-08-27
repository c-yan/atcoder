from itertools import accumulate

N, T, *A = map(int, open(0).read().split())

t = [0] * (10 ** 6 + T + 1)
for a in A:
    t[a] += 1
    t[a + T] -= 1

print(len(t) - list(accumulate(t)).count(0))
