n, m, p = map(int, input().split())
result = 1
n %= m
t = n
result = 1
while p != 0:
    if p % 2 == 1:
        result = (result * t) % m
    p //= 2
    t = (t * t) % m
print(result)
