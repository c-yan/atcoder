# imos 法
N = int(input())
a = list(map(int, input().split()))

t = [0] * (10 ** 5 + 3)  # t[X + 1] は ai = X となる i の個数
for x in a:
    t[x] += 1
    t[x + 3] -= 1

for i in range(1, 10 ** 5 + 3):
    t[i] += t[i-1]

print(max(t))
