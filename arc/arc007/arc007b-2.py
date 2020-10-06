N, M = map(int, input().split())

result = list(range(N + 1))
for _ in range(M):
    disk = int(input())
    i = result.index(disk)
    result[0], result[i] = disk, result[0]
print(*result[1:], sep='\n')
