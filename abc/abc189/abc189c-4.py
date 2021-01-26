N, *A = map(int, open(0).read().split())

r = [0] * N
for i in range(N - 1, -1, -1):
    j = i + 1
    while j < N:
        if A[j] < A[i]:
            break
        j = r[j]
    r[i] = j

result = 0
l = [0] * N
for i in range(N):
    j = i
    while j > 0:
        if A[j - 1] < A[i]:
            break
        j = l[j - 1]
    l[i] = j
    result = max(result, A[i] * (r[i] - l[i]))
print(result)
