S = input()

result = 0
for c in S:
    if c == '+':
        result += 1
    elif c == '-':
        result -= 1
print(result)
