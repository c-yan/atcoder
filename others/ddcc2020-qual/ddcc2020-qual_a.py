X, Y = map(int, input().split())


def f(n):
    if n == 3:
        return 100000
    elif n == 2:
        return 200000
    elif n == 1:
        return 300000
    else:
        return 0


result = f(X) + f(Y)
if X == 1 and Y == 1:
    result += 400000
print(result)
