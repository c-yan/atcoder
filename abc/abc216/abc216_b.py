N = int(input())

t = set()
for _ in range(N):
    S, T = input().split()
    t.add(S + ' ' + T)

if len(t) != N:
    print('Yes')
else:
    print('No')
