N = int(input())

result = False
t = 0
for _ in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        t += 1
    else:
        t = 0
    if t >= 3:
        result = True
        break

if result:
    print('Yes')
else:
    print('No')
