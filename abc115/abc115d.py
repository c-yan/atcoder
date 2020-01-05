N, X = map(int, input().split())


def f(N, X):
    result = 0

    if X >= 1:
        X -= 1
    else:
        return result

    if X >= 2 ** ((N - 1) + 2) - 3:
        X -= 2 ** ((N - 1) + 2) - 3
        result += 2 ** ((N - 1) + 1) - 1
    else:
        return result + f(N - 1, X)

    if X >= 1:
        X -= 1
        result += 1
    else:
        return result

    if X >= 2 ** ((N - 1) + 2) - 3:
        X -= 2 ** ((N - 1) + 2) - 3
        result += 2 ** ((N - 1) + 1) - 1
    else:
        return result + f(N - 1, X)

    if X >= 1:
        X -= 1
    else:
        return result

    return result


print(f(N, X))
