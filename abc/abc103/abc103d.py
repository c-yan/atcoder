N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])

result = 0
t = -1
for a, b in ab:
    a, b = a - 1, b - 1
    if a <= t < b:
        continue
    result += 1
    t = b - 1
print(result)
