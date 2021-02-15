s = input()

i = 0
c = 0
result = 0
while i < len(s):
    if s[i] == 'A':
        c += 1
    elif s[i] == 'B':
        if i == len(s) - 1 or s[i + 1] != 'C' or c == 0:
            c = 0
            i += 1
            continue
        result += c
        i += 1
    elif s[i] == 'C':
        c = 0
    i += 1
print(result)
