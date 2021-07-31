X = list(map(int, input()))

if X.count(X[0]) == 4 or all(X[i + 1] == (X[i] + 1) % 10 for i in range(3)):
    print('Weak')
else:
    print('Strong')
