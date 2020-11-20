A, B = map(int, input().split())

if any(A * B * C % 2 == 1 for C in range(1, 4)):
    print('Yes')
else:
    print('No')
