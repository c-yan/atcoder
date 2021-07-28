N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = K - sum(abs(A[i] - B[i]) for i in range(N))
if x >= 0 and x % 2 == 0:
    print('Yes')
else:
    print('No')
