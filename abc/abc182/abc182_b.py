N, *A = map(int, open(0).read().split())

result = 0
for i in range(2, 1000):
    t = 0
    for a in A:
        if a % i == 0:
            t += 1
    result = max(result, t)
print(result)
