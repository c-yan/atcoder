from itertools import accumulate

N = int(input())
S = input()
W = list(map(int, input().split()))

a = sorted(W)
d = {}
for i in range(len(a)):
    d[a[i]] = i + 1
W = [d[x] for x in W]
m = max(W)

b = [0] * (m + 2)
c = [0] * (m + 2)
for i in range(N):
    if S[i] == '0':
        b[W[i]] += 1
    else:
        c[W[i]] += 1
b = list(accumulate(b))
c = list(accumulate(c))
d = S.count('1')

result = 0
for i in range(m + 2):
    result = max(result, b[i] + (d - c[i]))
print(result)
