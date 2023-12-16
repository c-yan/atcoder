A, B, C = map(int, input().split())

if A != min([A, B, C]) and A != max([A, B, C]):
    print('A')
elif B != min([A, B, C]) and B != max([A, B, C]):
    print('B')
elif C != min([A, B, C]) and C != max([A, B, C]):
    print('C')
