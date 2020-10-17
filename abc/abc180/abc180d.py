X, Y, A, B = map(int, input().split())

result = 0
while X <= (Y - 1) // A and X * (A - 1) < B:
    X *= A
    result += 1

result += ((Y - 1) - X) // B

print(result)
