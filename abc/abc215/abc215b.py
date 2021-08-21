N = int(input())

for k in range(100):
    if 2 ** k <= N:
        continue
    result = k - 1
    break
print(result)
