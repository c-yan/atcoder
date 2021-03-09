from itertools import permutations

A = list(map(int, input().split()))

result = 10 ** 18
for p in permutations(A):
    b = p[0]
    c = 0
    for a in p:
        c += abs(a - b)
        b = a
    result = min(result, c)
print(result)
