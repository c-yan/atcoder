N = int(input())
p = list(map(int, input().split()))

z = 0
for i in range(N):
    if p[i] != i + 1:
        z += 1
if z <= 2:
    print('YES')
else:
    print('NO')
