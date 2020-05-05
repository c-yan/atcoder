N = int(input())
data = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        C, S, F = data[j]
        if t < S:
            t = S + C
        else:
            t += (t % F) + C
    print(t)
print(0)
