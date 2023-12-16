m = 998244353

A, B, C = map(int, input().split())

a = A * (A + 1) // 2
b = B * (B + 1) // 2
c = C * (C + 1) // 2

print(a * b * c % m)
