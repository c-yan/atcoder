A1, A2, A3 = map(int, input().split())

if sum([A1, A2, A3]) >= 22:
    print('bust')
else:
    print('win')
