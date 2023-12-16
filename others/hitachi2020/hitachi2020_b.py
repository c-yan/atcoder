A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    t = a[x - 1] + b[y - 1] - c
    if t < result:
        result = t
print(result)
