N, L = map(int, input().split())
S = input()

result = 0
tabs = 1
for c in S:
    if c == '+':
        tabs += 1
    elif c == '-':
        tabs -= 1

    if tabs > L:
        result += 1
        tabs = 1
print(result)
