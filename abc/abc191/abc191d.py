def main():
    from decimal import Decimal
    from math import floor, ceil, sqrt

    X, Y, R = map(Decimal, input().split())

    result = 0
    X10000 = int(X * 10000)
    Y10000 = int(Y * 10000)
    R10000 = int(R * 10000)
    X = float(X)
    Y = float(Y)
    R = float(R)

    RR = R10000 * R10000

    def check(x, y):
        x10000 = x * 10000
        y10000 = y * 10000
        return (x10000 - X10000) * (x10000 - X10000) + (y10000 - Y10000) * (y10000 - Y10000) <= RR

    for y in range(int(Y - R) - 10, int(Y + R) + 10 + 1):
        a = 1
        b = -2 * X
        c = X * X + (y - Y) * (y - Y) - R * R
        try:
            x0 = int((-b - sqrt(b * b - 4 * a * c)) / 2 * a)
            x1 = int((-b + sqrt(b * b - 4 * a * c)) / 2 * a)
        except:
            continue
        for x in range(x0 - 5, x0 + 5):
            if check(x, y):
                x0 = x
                break
        else:
            continue
        for x in range(x1 + 5, x1 - 5, -1):
            if check(x, y):
                x1 = x
                break
        else:
            continue
        result += (x1 - x0) + 1
    print(result)


main()
