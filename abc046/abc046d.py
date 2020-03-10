s = input()

g = s.count('g')
p = s.count('p')

t = list(s)
for i in range(len(s) - 1, -1, -1):
    if t[i] == 'g' and g > p + 1:
        t[i] = 'p'
        g -= 1
        p += 1
t = ''.join(t)

result = 0
for i in range(len(s)):
    if t[i] == 'p' and s[i] == 'g':
        result += 1
    elif t[i] == 'g' and s[i] == 'p':
        result -= 1
print(result)
