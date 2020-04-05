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
    print('\n'.join(str(r) for r in R))
if B:
    print('\n'.join(str(b) for b in B))
