# 解説の疑似のコードを Python で実装
N, M = map(int, input().split())

num = [1] * N
red = [False] * N
red[0] = True
for i in range(M):
    x, y = map(int, input().split())
    if red[x - 1]:
        red[y - 1] = True
    num[x - 1] -= 1
    num[y - 1] += 1
    if num[x - 1] == 0:
        red[x - 1] = False
print(red.count(True))
