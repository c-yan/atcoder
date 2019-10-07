N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

result = 0
for i in range(N):
    if V[i] > C[i]:
        result += V[i] - C[i]
print(result)
