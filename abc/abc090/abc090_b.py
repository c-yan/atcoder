A, B = map(int, input().split())


def f(n):
    result = 0
    for i in range(10000, n + 1):
        t = str(i)
        if t == t[::-1]:
            result += 1
    return result


print(f(B) - f(A - 1))
