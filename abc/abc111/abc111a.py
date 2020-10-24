n = input()

result = ''
for c in n:
    if c == '1':
        result += '9'
    elif c == '9':
        result += '1'
    else:
        result += c
print(result)
