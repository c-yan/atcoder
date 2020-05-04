S = input()


def f(s):
    i = s.find('(')
    if i == -1:
        return s

    result = s[:i]
    s = s[i:]
    i = 1
    n = 1
    while n != 0:
        if s[i] == '(':
            n += 1
        elif s[i] == ')':
            n -= 1
        i += 1
    t = f(s[1:i - 1])
    result += t + t[::-1]
    result += f(s[i:])
    return result


print(f(S))
