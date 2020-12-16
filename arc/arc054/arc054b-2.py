P = float(input())

def f(x):
    return x + P / 2 ** (x / 1.5)

ratio = (1 + 5 ** 0.5) / 2
l = 0
r = min(P, 2e+3)
a = f((l * ratio + r) / (1 + ratio))
b = f((l + r * ratio) / (1 + ratio))
for _ in range(100):
    if a < b:
        r = (l + r * ratio) / (1 + ratio)
        b = a
        a = f((l * ratio + r) / (1 + ratio))
    else:
        l = (l * ratio + r) / (1 + ratio)
        a = b
        b = f((l + r * ratio) / (1 + ratio))
print(f((l + r) / 2))
