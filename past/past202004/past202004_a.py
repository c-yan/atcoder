S, T = input().split()


def f(s):
    if s[0] == 'B':
        return -int(s[1])
    else:
        return int(s[0]) - 1


print(abs(f(S) - f(T)))
