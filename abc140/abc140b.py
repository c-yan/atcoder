N = int(input())
A = [int(e) - 1 for e in input().split()]
B = list(map(int, input().split()))
C = list(map(int, input().split()))
before = N
result = 0
for i in range(N):
  result += B[A[i]]
  if before + 1 == A[i]:
    result += C[before]
  before = A[i]
print(result)
