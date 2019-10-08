A, B, C = map(int, input().split())

result = 0
while True:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        break
    if A == B == C:
        result = -1
        break
    A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
    result += 1
print(result)
