N = int(input())
T = list(map(int, input().split()))
M = int(input())

x = sum(T)
for _ in range(M):
    P, X = map(int, input().split())
    print(x - T[P - 1] + X)
