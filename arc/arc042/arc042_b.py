x, y = map(int, input().split())
N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

result = 10 ** 18
for i in range(N):
    x1, y1 = xy[i - 1]
    x2, y2 = xy[i]
    if x1 == x2:
        result = min(result, abs(x - x1))
        continue
    if y1 == y2:
        result = min(result, abs(y - y1))
        continue
    a = (y2 - y1) / (x2 - x1)
    b = -1
    c = a * -x1 + y1
    d = abs(a * x + b * y + c) / ((a * a + b * b) ** 0.5)
    result = min(result, d)
print(result)
