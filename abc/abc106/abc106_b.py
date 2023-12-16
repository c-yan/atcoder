N = int(input())

result = 0
for i in range(1, N + 1, 2):
    t = 0
    for j in range(1, i + 1):
        if i % j == 0:
            t += 1
    if t == 8:
        result += 1
print(result)
