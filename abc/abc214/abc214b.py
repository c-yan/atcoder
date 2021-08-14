S, T = map(int, input().split())

result = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a + b + c > S:
                break
            if a * b * c > T:
                break
            result += 1
print(result)
