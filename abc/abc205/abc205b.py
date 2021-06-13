N, *A = map(int, open(0).read().split())

A.sort()
for i in range(N):
    if i == A[i] - 1:
        continue
    print('No')
    break
else:
    print('Yes')
