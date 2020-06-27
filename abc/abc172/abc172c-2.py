# Two Pointer
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

b_sum = sum(B)
for i in range(M - 1, -1, -1):
    if b_sum <= K:
        j = i
        break
    b_sum -= B[i]
else:
    j = -1
result = j + 1

a_sum = 0
for i in range(N):
    a_sum += A[i]
    if a_sum > K:
        break
    while a_sum + b_sum > K:
        b_sum -= B[j]
        j -= 1
    result = max(result, (i + 1) + (j + 1))
print(result)
