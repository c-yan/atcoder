N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    if A == B:
        print(-1)
    else:
        print(abs(A - B))
