X, K, D = map(int, input().split())

if X > D:
    t = min(X // D, K)
    K -= t
    X -= t * D
else:
    t = min(-X // D, K)
    K -= t
    X += t * D

K %= 2

if K == 0:
    print(abs(X))
else:
    if abs(X + D) < abs(X - D):
        print(abs(X + D))
    else:
        print(abs(X - D))
