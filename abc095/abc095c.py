a, b, c, x, y = map(int, input().split())
result = 0
if a + b > 2 * c:
    t = min(x, y)
    result += t * 2 * c
    x, y = x - t, y - t
else:
    t = min(x, y)
    result += t * a + t * b
    x, y = x - t, y - t
if x > 0:
    if a > 2 * c:
        result += x * 2 * c
    else:
        result += x * a
else:
    if b > 2 * c:
        result += y * 2 * c
    else:
        result += y * b
print(result)
