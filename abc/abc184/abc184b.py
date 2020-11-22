N, X = map(int, input().split())
S = input()

result = X
for c in S:
    if c == 'o':
        result += 1
    elif c == 'x':
        if result != 0:
            result -= 1
print(result)
