N, T, *A = map(int, open(0).read().split())

A.sort()
result = 0
o = -1
for a in A:
    if o != -1 and a > c:
        result += c - o
        o = -1
        c = -1
    if o == -1:
        o = a
        c = a + T
    else:
        c = a + T
result += c - o
print(result)
