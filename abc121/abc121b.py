N, M, C = map(int, input().split())
B = list(map(int, input().split()))

result = 0
for i in range(N):
    t = C
    A = list(map(int, input().split()))
    for j in range(M):
        t += A[j] * B[j]
    if t > 0:
        result += 1
print(result)
