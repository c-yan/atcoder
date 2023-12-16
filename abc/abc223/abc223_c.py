from sys import stdin

readline = stdin.readline

N = int(readline())
AB = [tuple(map(int, readline().split())) for _ in range(N)]

s = sum(a / b for a, b in AB) / 2
result = 0
for a, b in AB:
    if s - a / b <= 0:
        result += s * b
        break
    s -= a / b
    result += a
print(result)
