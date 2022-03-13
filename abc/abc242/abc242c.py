m = 998244353

N = int(input())

t = [1] * 10
t[0] = 0

for i in range(N - 1):
    u = [0] * 10
    for i in range(1, 10):
        for j in [-1, 0, 1]:
            k = i + j
            if k < 1 or k > 9:
                continue
            u[k] += t[i]
            u[k] %= m
    t = u
print(sum(t) % m)
