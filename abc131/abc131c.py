from fractions import gcd

a, b, c, d = [int(e) for e in input().split()]

def f(a, b, n):
  return b // n - (a - 1) // n

acc = 0
acc += f(a, b, c)
acc += f(a, b, d)
acc -= f(a, b, c * d // gcd(c, d))
print(b - a + 1 - acc)
