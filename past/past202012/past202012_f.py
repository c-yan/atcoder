from itertools import product

N, M = map(int, input().split())
ABC = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

def is_exploded(p):
    for a, b, c in ABC:
        if p[a] and p[b] and p[c]:
            return True
    return False

result = 0
for p in product([True, False], repeat=N):
    if is_exploded(p):
        continue
    t = set()
    for a, b, c in ABC:
        if p[a] and p[b]:
            t.add(c)
        elif p[a] and p[c]:
            t.add(b)
        elif p[b] and p[c]:
            t.add(a)
    result = max(result, len(t))
print(result)
