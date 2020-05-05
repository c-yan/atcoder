# imos 法
n = int(input())
cs = [0] * (1000000 + 1)
for _ in range(n):
    a, b = map(int, input().split())
    cs[a] += 1
    if b != 1000000:
        cs[b + 1] -= 1
for i in range(1, 1000000 + 1):
    cs[i] += cs[i - 1]
print(max(cs))
