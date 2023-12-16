N, X, Y, *A = map(int, open(0).read().split())

sections = []
t = []
for i in range(N):
    if A[i] > X or A[i] < Y:
        if len(t) != 0:
            sections.append(t)
            t = []
        continue
    t.append(A[i])
if len(t) != 0:
    sections.append(t)


def asplit(a, sep):
    t = []
    for e in a:
        if e in sep:
            if len(t) != 0:
                yield t
                t = []
            continue
        t.append(e)
    if len(t) != 0:
        yield t


result = 0
for s in sections:
    c = len(s) * (len(s) - 1) // 2
    for t in asplit(s, [X]):
        c -= len(t) * (len(t) - 1) // 2
    for t in asplit(s, [Y]):
        c -= len(t) * (len(t) - 1) // 2
    for t in asplit(s, [X, Y]):
        c += len(t) * (len(t) - 1) // 2
    result += c
if X == Y:
    result += A.count(X)
print(result)
