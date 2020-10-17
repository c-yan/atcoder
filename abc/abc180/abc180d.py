X, Y, A, B = map(int, input().split())

result = 0
t = X

while t * (A - 1) < B:
    if t * A >= Y:
        break
    t *= A
    result += 1

n = ((Y - 1) - t) // B
t += B * n
result += n

print(result)
