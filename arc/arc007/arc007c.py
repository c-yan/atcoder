from itertools import product

c = input()
N = len(c)


def is_ok(p, i):
    for j in range(N):
        if not p[j]:
            continue
        if c[(i + (N - 1) - j) % N] == 'o':
            return True
    return False


result = 10 ** 18
for p in product([True, False], repeat=N):
    if all(is_ok(p, i) for i in range(N)):
        result = min(result, p.count(True))
print(result)
