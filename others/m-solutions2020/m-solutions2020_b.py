A, B, C = map(int, input().split())
K = int(input())

while A >= B:
    K -= 1
    B *= 2

while B >= C:
    K -= 1
    C *= 2

if K >= 0:
    print('Yes')
else:
    print('No')
