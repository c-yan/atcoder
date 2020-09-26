A, B, C, D = map(int, input().split())

if A <= C <= B or A <= D <= B or C <= A <= D or C <= B <= D:
    print('Yes')
else:
    print('No')
