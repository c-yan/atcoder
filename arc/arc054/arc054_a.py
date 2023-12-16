L, X, Y, S, D = map(int, input().split())

d = D - S
if d < 0:
    d += L
result = d / (X + Y)

if Y - X > 0:
    d = S - D
    if d < 0:
        d += L
    result = min(result, d / (Y - X))

print(result)
