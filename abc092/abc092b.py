N = int(input())
D, X = map(int, input().split())

for _ in range(N):
    A = int(input())
    X += (D - 1) // A + 1
print(X)
