N = int(input())
a = list(map(int, input().split()))

t = [0] * (10 ** 5 + 3)  # t[X + 1] は ai = X となる i の個数
for x in a:
    for i in range(x - 1, x + 2):
        t[i] += 1
print(max(t))
