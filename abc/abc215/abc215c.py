from itertools import permutations

S, K = input().split()
K = int(K)

print(sorted(set(''.join(p) for p in permutations(S)))[K - 1])
