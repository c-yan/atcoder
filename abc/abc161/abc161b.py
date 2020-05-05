N, M = map(int, input().split())
A = list(map(int, input().split()))

threshold = sum(A) / (4 * M)
if len([a for a in A if a >= threshold]) >= M:
    print('Yes')
else:
    print('No')
