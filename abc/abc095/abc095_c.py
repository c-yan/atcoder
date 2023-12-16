A, B, C, X, Y = map(int, input().split())

result = 0
if A + B > 2 * C:
    t = min(X, Y)
    result += t * 2 * C
    X, Y = X - t, Y - t
else:
    t = min(X, Y)
    result += t * A + t * B
    X, Y = X - t, Y - t
if X > 0:
    if A > 2 * C:
        result += X * 2 * C
    else:
        result += X * A
else:
    if B > 2 * C:
        result += Y * 2 * C
    else:
        result += Y * B
print(result)
