N = int(input())

PS = []
for _ in range(N):
    S, P = input().split()
    P = int(P)
    PS.append((P, S))

PS.sort(reverse=True)
total = sum(P for P, S in PS)
if PS[0][0] > total // 2:
    print(PS[0][1])
else:
    print('atcoder')
