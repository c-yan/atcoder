N, K = map(int, input().split())
A = list(map(int, input().split()))

bcs = [0] * 41
for i in range(N):
    a = A[i]
    for j in range(41):
        if a & (1 << j) != 0:
            bcs[j] += 1

X = 0
for i in range(40, -1, -1):
    if bcs[i] >= N - bcs[i]:
        continue
    t = 1 << i
    if X + t <= K:
        X += t

result = 0
for i in range(N):
    result += X ^ A[i]
print(result)
