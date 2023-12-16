N = int(input())

t = 1
c = 0
while t <= N:
    t *= 1000
    c += 1
t //= 1000
c -= 1

result = 0
while t != 1:
    result += c * (N - t + 1)
    N = t - 1
    t //= 1000
    c -= 1
print(result)
