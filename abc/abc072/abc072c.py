N, *a = map(int, open(0).read().split())

t = [0] * (10 ** 5 + 2)  # t[X + 1] は操作により ai = X となりうる i の個数
for x in a:
    for i in range(x, x + 3):
        t[i] += 1
print(max(t))
