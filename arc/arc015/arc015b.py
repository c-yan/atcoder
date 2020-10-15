N = int(input())

result = [0] * 6
for _ in range(N):
    MT, mT = map(float, input().split())
    if MT >= 35:
        result[0] += 1
    if 30 <= MT < 35:
        result[1] += 1
    if 25 <= MT < 30:
        result[2] += 1
    if mT >= 25:
        result[3] += 1
    if mT < 0 and MT >= 0:
        result[4] += 1
    if MT < 0:
        result[5] += 1
print(*result)
