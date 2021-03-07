N = int(input())

t = 0
for i in range(1, N + 1):
    t += 1 / i
print(N * t - 1)
