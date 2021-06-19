N = int(input())

t = N * 108 // 100
if t < 206:
    print('Yay!')
elif t == 206:
    print('so-so')
elif t > 206:
    print(':(')
