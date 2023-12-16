N, A, B = map(int, input().split())


def clamp(x, y, z):
    if x < y:
        return y
    elif x > z:
        return z
    else:
        return x


result = 0
for _ in range(N):
    s, d = input().split()
    d = int(d)
    if s == 'West':
        result -= clamp(d, A, B)
    if s == 'East':
        result += clamp(d, A, B)

if result == 0:
    print(0)
elif result < 0:
    print('West', -result)
else:
    print('East', result)
