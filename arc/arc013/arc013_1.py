from itertools import permutations

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

result = 0
for a, b, c in permutations((P, Q, R)):
    result = max(result, (N // a) * (M // b) * (L // c))
print(result)
