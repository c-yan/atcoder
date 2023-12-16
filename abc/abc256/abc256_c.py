h1, h2, h3, w1, w2, w3 = map(int, input().split())

result = 0
for v11 in range(1, h1 - 1):
    for v21 in range(1, h1 - v11):
        v31 = h1 - v11 - v21
        for v12 in range(1, h2 - 1):
            for v22 in range(1, h2 - v12):
                v32 = h2 - v12 - v22
                if v32 < 1:
                    continue
                v13 = w1 - v11 - v12
                if v13 < 1:
                    continue
                v23 = w2 - v21 - v22
                if v23 < 1:
                    continue
                v33 = w3 - v31 - v32
                if v33 < 1:
                    continue
                if v13 + v23 + v33 != h3:
                    continue
                result += 1
print(result)
