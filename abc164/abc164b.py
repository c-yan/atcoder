A, B, C, D = map(int, input().split())

while True:
    C -= B
    if C <= 0:
        break
    A -= D
    if A <= 0:
        break

if A > 0:
    print('Yes')
else:
    print('No')
