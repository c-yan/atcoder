X = input()

for _ in range(50):
    if len(X) >= 2 and X[-2:] == 'ch':
        X = X[:-2]
    elif len(X) >= 1 and X[-1] in 'oku':
        X = X[:-1]

if X == '':
    print('YES')
else:
    print('NO')
