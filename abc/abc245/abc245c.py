N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = True
b = True
for i in range(1, N):
    c, d = a, b
    a = (c and abs(A[i - 1] - A[i]) <= K) or (d and abs(B[i - 1] - A[i]) <= K)
    b = (c and abs(A[i - 1] - B[i]) <= K) or (d and abs(B[i - 1] - B[i]) <= K)

if a or b:
    print('Yes')
else:
    print('No')
