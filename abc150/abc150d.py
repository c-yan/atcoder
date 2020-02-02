from fractions import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))

a = A[0]
n = 1
while a % 2 == 0:
    n *= 2
    a //= 2

lcm = 1
for a in A:
    if a % n != 0 or a % (2 * n) == 0:
        print(0)
        exit()
    lcm = lcm * a // gcd(lcm, a)
    if lcm // 2 > M:
        print(0)
        exit()

print((M - lcm // 2) // lcm + 1)
