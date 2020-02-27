s = input()

result = ''
for c in s:
    if c == '0' or c == '1':
        result += c
    elif c == 'B':
        result = result[:-1]
print(result)
