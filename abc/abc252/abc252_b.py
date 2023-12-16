N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = max(A)
if len(set(B) & set(i + 1 for i in range(N) if A[i] == x)) > 0:
    print('Yes')
else:
    print('No')
