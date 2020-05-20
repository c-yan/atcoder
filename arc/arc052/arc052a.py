S = input()

result = 0
for c in S:
    if '0' <= c <= '9':
        result = result * 10 + int(c)
print(result)
