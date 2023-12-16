from itertools import accumulate

m = 1000000007

N = int(input())
S = input()

a = [1] * N
for c in 'atcoder':
    b = [0] * N
    for i in range(N):
        if S[i] != c:
            continue
        b[i] = a[i] % m
    a = list(accumulate(b))
print(a[-1] % m)
