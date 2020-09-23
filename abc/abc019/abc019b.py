s = input()

p = s[0]
t = 0
result = ''
for c in s:
    if p == c:
        t += 1
        continue
    result += '%s%d' % (p, t)
    p = c
    t = 1
result += '%s%d' % (p, t)
print(result)
