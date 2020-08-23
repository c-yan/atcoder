a = int(input())
b = int(input())

if a > b:
    a, b = b, a
print(min(b - a, 10 - (b - a)))
