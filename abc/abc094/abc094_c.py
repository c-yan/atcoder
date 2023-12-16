N = int(input())
X = list(map(int, input().split()))

y = sorted(X)
a = y[N // 2 - 1]
b = y[N // 2]
for i in range(N):
    if X[i] >= b:
        print(a)
    else:
        print(b)
