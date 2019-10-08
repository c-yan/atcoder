N = int(input())
A = list(map(int, input().split()))

v = 0
for i in range(N):
    v += 1 / A[i]
print(1 / v)
