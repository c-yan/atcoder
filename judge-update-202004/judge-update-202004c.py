from itertools import permutations

a1, a2, a3 = map(int, input().split())
a = [a1, a2, a3]

N = a1 + a2 + a3
result = 0
for p in permutations(range(1, N + 1)):
    X = [p[:a1], p[a1:a1 + a2], p[a1 + a2:]]
    flag = True
    for i in range(3):
        for j in range(1, a[i]):
            if X[i][j] <= X[i][j - 1]:
                flag = False
    for i in range(1, 3):
        for j in range(a[i]):
            if X[i][j] <= X[i - 1][j]:
                flag = False
    if flag:
        result += 1
print(result)
