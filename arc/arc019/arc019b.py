A = input()

def f(s):
    t = s[::-1]
    c = 0
    for i in range(len(s) // 2):
        if s[i] != t[i]:
            c += 1
    return c

c = f(A)
if len(A) % 2 == 0:
    if c == 0 or c >= 2:
        print(25 * len(A))
    elif c == 1:
        print(25 * len(A) - 2)
elif len(A) % 2 == 1:
    if c == 0:
        print(25 * (len(A) - 1))
    elif c == 1:
        print(25 * len(A) - 2)
    elif c >= 2:
        print(25 * len(A))
