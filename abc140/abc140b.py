N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
before = N
result = 0
for i in range(N):
  result += B[A[i] - 1]
  if before + 1 == A[i] - 1:
    result += C[before]
  before = A[i] - 1
print(result)
