V, T, S, D = map(int, input().split())

if T * V <= D <= S * V:
    print('No')
else:
    print('Yes')
