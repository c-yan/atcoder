N, M = map(int, input().split())
A = list(map(int, input().split()))

a = sum(A)

if a > N:
    print(-1)
else:
    print(N - a)
