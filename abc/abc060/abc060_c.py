N, T = map(int, input().split())
t = list(map(int, input().split()))

X = 0
for i in range(1, N):
    X += min(t[i] - t[i - 1], T)
X += T

print(X)
