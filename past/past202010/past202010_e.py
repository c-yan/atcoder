from itertools import permutations

N = int(input())
S = input()

for p in permutations(S):
    T = ''.join(p)
    if T == S or T == S[::-1]:
        continue
    print(T)
    break
else:
    print('None')
