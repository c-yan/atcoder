P = float(input())

def f(x):
    return x + P / 2 ** (x / 1.5)

l = 0
r = min(P, 2e+3)
for _ in range(100):
    a = f((l * 2 + r) / 3)
    b = f((l + r * 2) / 3)
    if a < b:
        r = (l + r * 2) / 3
    else:
        l = (l * 2 + r) / 3
print(f((l + r) / 2))
