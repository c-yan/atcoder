N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
y = [X[i] - X[i - 1] for i in range(1, M)]
y.sort()
print(sum(y[:M - N]) if N < M else 0)
