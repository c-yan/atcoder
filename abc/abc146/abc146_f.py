N, M = map(int, input().split())
S = input()

t = S[::-1]
i = 0
result = []
while i != N:
    for j in range(M, 0, -1):
        if i + j > N:
            continue
        if t[i + j] == '1':
            continue
        i = i + j
        result.append(j)
        break
    else:
        print(-1)
        exit()
print(*result[::-1])
