N, M, T = map(int, input().split())

n = N
p = 0
for _ in range(M):
    A, B = map(int, input().split())
    n -= A - p
    if n <= 0:
        print('No')
        exit()
    n = min(N, n + B - A)
    p = B
n -= T - p
if n <= 0:
    print('No')
    exit()
print('Yes')
