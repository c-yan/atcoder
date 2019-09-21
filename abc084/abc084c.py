n = int(input())
data = [list(map(int, input().split())) for _ in range(n - 1)]
for i in range(n - 1):
    t = 0
    for j in range(i, n - 1):
        c, s, f = data[j]
        if t < s:
            t = s + c
        else:
            t += (t % f) + c
    print(t)
print(0)
