N, *A = map(int, open(0).read().split())

result = 0
p = A[0]
for i in range(1, N):
    if p >= A[i]:
        result += p - A[i]
    else:
        p = A[i]
print(result)
