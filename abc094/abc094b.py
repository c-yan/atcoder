N, M, X = map(int, input().split())
A = set(map(int, input().split()))

print(min(len([i for i in range(1, X) if i in A]), len([i for i in range(X + 1, N) if i in A])))
