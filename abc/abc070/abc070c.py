from fractions import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


N = int(input())

result = 1
for _ in range(N):
    T = int(input())
    result = lcm(result, T)
print(result)
