A, R, N = map(int, input().split())

result = A
a = R
b = N - 1
while b != 0 and result <= 1000000000:
    if b & 1 != 0:
        result *= a
    a *= a
    b >>= 1

if result > 1000000000:
    print('large')
else:
    print(result)
