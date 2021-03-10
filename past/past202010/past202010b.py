X, Y = map(int, input().split())

if Y == 0:
    print('ERROR')
    exit()

print(('%.2f' % (int(X * 100 / Y) / 100))
