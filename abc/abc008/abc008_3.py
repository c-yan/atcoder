N, *C = map(int, open(0).read().split())

result = 0
for i in range(N):
    c = -1
    for j in range(N):
        if C[i] % C[j] == 0:
            c += 1
    result += (c // 2 + 1) / (c + 1)
print(result)
