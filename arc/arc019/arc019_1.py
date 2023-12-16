S = input()

t = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}

result = ''
for c in S:
    if c in t:
        result += t[c]
    else:
        result += c
print(result)
