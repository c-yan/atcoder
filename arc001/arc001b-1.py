INF = float('inf')

A, B = map(int, input().split())

result = 0
while A != B:
    d = INF
    na = INF
    for x in [1, -1, 5, -5, 10, -10]:
        t = A + x
        if abs(t - B) < d:
            d = abs(t - B)
            na = t
    A = na
    result += 1
print(result)
