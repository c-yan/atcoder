from itertools import accumulate

N, *A = map(int, open(0).read().split())

a = list(accumulate(A))

result = 0
c = 0
m = 0
for i in range(N):
    m = max(a[i], m)
    result = max(result, c + m)
    c += a[i]
print(result)
