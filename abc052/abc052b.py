N = int(input())
S = input()

result = 0
x = 0
for c in S:
    if c == 'I':
        x += 1
        result = max(result, x)
    elif c == 'D':
        x -= 1
print(result)
