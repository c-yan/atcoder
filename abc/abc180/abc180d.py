X, Y, A, B = map(int, input().split())

result = 0
while X * A < Y and X * A < X + B:
    X *= A
    result += 1
result += ((Y - 1) - X) // B
print(result)
