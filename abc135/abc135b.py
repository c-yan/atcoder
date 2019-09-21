n = int(input())
p = [int(e) for e in input().split()]
z = 0
for i in range(n):
    if p[i] != i + 1:
        z += 1
if z <= 2:
    print('YES')
else:
    print('NO')
