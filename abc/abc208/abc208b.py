P = int(input())

x = 3628800
y = 10

result = 0
while y != 0:
    n = P // x
    if n != 0:
        result += n
        P -= n * x
    x //= y
    y -= 1
print(result)
