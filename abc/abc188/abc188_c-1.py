N, *A = map(int, open(0).read().split())

a = range(2 ** N)
while len(a) != 2:
    t = []
    for i in range(0, len(a), 2):
        if A[a[i]] > A[a[i + 1]]:
            t.append(a[i])
        else:
            t.append(a[i + 1])
    a = t
if A[a[0]] > A[a[1]]:
    print(a[1] + 1)
else:
    print(a[0] + 1)
