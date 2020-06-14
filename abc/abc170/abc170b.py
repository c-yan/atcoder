X, Y = map(int, input().split())

for i in range(X + 1):
    if i * 2 + (X - i) * 4 == Y:
        print('Yes')
        break
else:
    print('No')
