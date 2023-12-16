N, X = map(int, input().split())

c = 0
for i in range(N):
    V, P = map(int, input().split())
    c += V * P
    if c > X * 100:
        print(i + 1)
        break
else:
    print(-1)
