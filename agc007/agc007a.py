H, W = map(int, input().split())
A = [input() for _ in range(H)]

if H + W - 1 == sum(a.count('#') for a in A):
    print('Possible')
else:
    print('Impossible')
