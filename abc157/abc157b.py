A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

for _ in range(N):
    b = int(input())
    for y in range(3):
        for x in range(3):
            if A[y][x] == b:
                A[y][x] = -1

for y in range(3):
    f = True
    for x in range(3):
        if A[y][x] != -1:
            f = False
    if f:
        print('Yes')
        exit()

for x in range(3):
    f = True
    for y in range(3):
        if A[y][x] != -1:
            f = False
    if f:
        print('Yes')
        exit()

f = True
for x in range(3):
    if A[x][x] != -1:
        f = False
if f:
    print('Yes')
    exit()

f = True
for x in range(3):
    if A[2 - x][x] != -1:
        f = False
if f:
    print('Yes')
    exit()

print('No')
