N = int(input())

X = N / 1.08
if int(X) * 108 // 100 == N:
    print(int(X))
elif int(X + 1) * 108 // 100 == N:
    print(int(X + 1))
else:
    print(':(')
