P = int(input())

x = 3628800  # 10!
y = 10

result = 0
while P != 0:
    n = P // x
    if n != 0:
        result += n
        P -= n * x
    x //= y
    y -= 1
print(result)
