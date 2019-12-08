N = int(input())

evidences = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        evidences[i].append((x - 1, y))

result = 0
for i in range(1, 2 ** N):
    consistent = True
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        for x, y in evidences[j]:
            if (i >> x) & 1 != y:
                consistent = False
                break
        if not consistent:
            break
    if consistent:
        result = max(result, bin(i)[2:].count('1'))
print(result)
