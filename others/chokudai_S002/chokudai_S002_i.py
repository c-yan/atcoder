N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

i = 0
for j in range(1, N):
    a, b = AB[i]
    c, d = AB[j]
    e = (c + b - 1) // b
    f = (a + d - 1) // d
    if f < e:
        i = j

for j in range(N):
    if i == j:
        continue
    a, b = AB[i]
    c, d = AB[j]
    e = (c + b - 1) // b
    f = (a + d - 1) // d
    if f <= e:
        print(-1)
        break
else:
    print(i + 1)
