N = int(input())

t = [[0] * 10 for _ in range(10)]
for i in range(1, N + 1):
    s = str(i)
    t[int(s[0])][int(s[-1])] += 1

result = 0
for i in range(1, 10):
    for j in range(1, 10):
        result += t[i][j] * t[j][i]
print(result)
