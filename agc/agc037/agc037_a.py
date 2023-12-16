def divide_string(s):
    result = []
    prev, t = '', ''
    for i in range(len(s)):
        t += s[i]
        if prev != t:
            result.append(t)
            prev, t = t, ''
    if t != '':
        if len(result) == 1 or len(result[-2]) == 1:
            result[-1] = result[-1] + t
        else:
            result[-2] = result[-2] + t
    return result


S = input()

print(len(divide_string(S)))
