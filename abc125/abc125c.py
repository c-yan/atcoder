from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
c1 = [0] * (n + 1)
c2 = [0] * (n + 1)
for i in range(1, n + 1):
  c1[i] = gcd(c1[i - 1], a[i - 1])
  c2[n - i] = gcd(c2[n - i + 1], a[n - i])
print(max(gcd(c1[i], c2[i + 1]) for i in range(n)))
