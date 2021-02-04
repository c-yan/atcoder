N = int(input())
T = input()

n = (N + 2) // 3
s = '110' * n


def f(s, t):
    result = 0
    i = s.find(t) + 1
    while i != 0:
        result += 1
        i = s.find(t, i) + 1
    return result


a = f(s, T)
if a == 0:
    n += 1
    s = '110' * n
    a = f(s, T)
print(a * (10 ** 10 - n + 1))
