N, K, *a = map(int, open(0).read().split())

b = a[:]
for x in range(K):
    b[x::K] = sorted(b[x::K])

if sorted(a) == b:
    print('Yes')
else:
    print('No')
