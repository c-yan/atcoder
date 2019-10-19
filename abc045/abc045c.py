def f(s, t):
    if t == '':
        return sum(map(int, s.split('+')))
    else:
        return f(s + t[0], t[1:]) + f(s + '+' + t[0], t[1:])


S = input()
print(f(S[0], S[1:]))
