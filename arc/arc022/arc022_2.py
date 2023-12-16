N, *A = map(int, open(0).read().split())

l = 0
r = 0
result = 0
s = set()
while r < N:
    while A[r] in s:
        s.remove(A[l])
        l += 1
    s.add(A[r])
    r += 1
    result = max(result, r - l)
print(result)
