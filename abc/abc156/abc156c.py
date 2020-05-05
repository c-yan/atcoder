N = int(input())
X = list(map(int, input().split()))

P = int(sum(X) / N + 0.5)
print(sum((x - P) * (x - P) for x in X))
