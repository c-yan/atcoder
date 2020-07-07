N = int(input())

R = []
B = []
for _ in range(N):
    X, C = input().split()
    if C == 'R':
        R.append(int(X))
    elif C == 'B':
        B.append(int(X))

R.sort()
B.sort()
if R:
    print(*R, sep='\n')
if B:
    print(*B, sep='\n')
