S = input()


def f(s):
    i = s.find('(')
    if i == -1:
        return s

    result = s[:i]
    s = s[i + 1:]
    n = 1
    for i in range(len(s)):
        if s[i] == '(':
            n += 1
        elif s[i] == ')':
            n -= 1
        if n == 0:
            break
    t = f(s[:i])
    result += t + t[::-1]
    result += f(s[i + 1:])
    return result


print(f(S))
