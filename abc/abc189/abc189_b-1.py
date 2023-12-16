from decimal import Decimal

N, X = map(int, input().split())

c = 0
for i in range(N):
    V, P = map(Decimal, input().split())
    c += V * (P / 100)
    if c > X:
        print(i + 1)
        break
else:
    print(-1)
