H, W = map(int, input().split())
S = [input() for _ in range(H)]

result = [[] for _ in range(H)]
for y in range(H):
    Sy = S[y]
    resulty = result[y]
    for x in range(W):
        if Sy[x] == '#':
            resulty.append('#')
        else:
            t = 0
            for i in range(max(y - 1, 0), min(y + 2, H)):
                Si = S[i]
                for j in range(max(x - 1, 0), min(x + 2, W)):
                    if Si[j] == '#':
                        t += 1
            resulty.append(str(t))

for y in range(H):
    print(''.join(result[y]))
