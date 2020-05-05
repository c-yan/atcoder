H, N = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) >= H:
    print('Yes')
else:
    print('No')
