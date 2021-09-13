X, Y = map(int, open(0).read().split('.'))

if 0 <= Y <= 2:
    print('%d-' % X)
elif 3 <= Y <= 6:
    print('%d' % X)
elif 7 <= Y <= 9:
    print('%d+' % X)
