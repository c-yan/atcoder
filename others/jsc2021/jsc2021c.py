A, B = map(int, input().split())

for a in range(1, B + 1):
    x = (A + (a - 1)) // a * a
    y = x + a
    if x < A or y > B:
        continue
    result = a
print(result)
