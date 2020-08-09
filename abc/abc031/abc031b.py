L, H = map(int, input().split())
N = int(input())

for _ in range(N):
    A = int(input())
    if L <= A <= H:
        print(0)
    elif A > H:
        print(-1)
    elif A < L:
        print(L - A)
