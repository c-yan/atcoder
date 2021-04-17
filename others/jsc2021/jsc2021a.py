X, Y, Z = map(int, input().split())

if Y * Z % X == 0:
    print(Y * Z // X - 1)
else:
    print(Y * Z // X)
