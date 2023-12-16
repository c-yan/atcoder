N, *A = map(int, open(0).read().split())

# last: must, this: must
a = 0
# last: optional, this: optional
b = A[0]
# last: must, this: optional
c = 10 ** 15
# last: optional, this: must
d = 10 ** 15
for i in range(1, N - 1):
    # from a
    nc = a + A[i]
    # from b
    nb = b + A[i]
    nd = b
    # from c
    na = c
    nc = min(nc, c + A[i])
    # from d
    nb = min(nb, d + A[i])
    a = na
    b = nb
    c = nc
    d = nd
a += A[N - 1]
c += A[N - 1]
d += A[N - 1]
print(min(a, b, c, d))
