n, *a = map(int, open(0).read().split())

result = 0
for t in a:
    if t % 3 == 2:
        result += 1
        t -= 1
    if t % 2 == 0:
        result += 1
        t -= 1
    if t % 3 == 2:
        result += 1
        t -= 1
    if t % 2 == 0:
        result += 1
        t -= 1
print(result)
