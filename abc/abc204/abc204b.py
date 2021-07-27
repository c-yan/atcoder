N, *A = map(int, open(0).read().split())

result = 0
for a in A:
    if a <= 10:
        continue
    result += a - 10
print(result)
