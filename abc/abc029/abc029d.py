def f(n):
    if n == 0:
        return 0
    if n < 10:
        return 1
    s = str(n)
    if s.count('9') == len(s):
        return len(s) * 10 ** (len(s) - 1)
    a = int(s[0])
    b = int(s[1:])
    if a == 1:
        return f(n - b - 1) + (b + 1) + f(b)
    else:
        c = '9' * (len(s) - 1)
        return f(int('1' + c)) + (a - 2) * f(int(c)) + f(b)


N = int(input())
print(f(N))
