import math
n, d = map(int, input().split())
x = [[int(e) for e in input().split()] for _ in range(n)]
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        t = math.sqrt(sum((x[i][k] - x[j][k]) * (x[i][k] - x[j][k])
                          for k in range(d)))
        if t == math.ceil(t):
            result += 1
print(result)
