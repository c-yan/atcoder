s = input()
a = 0
b = 1
x = 0
y = 0
for i in range(len(s)):
    t = ord(s[i]) - 48
    if t != a:
        x += 1
    if t != b:
        y += 1
    a ^= 1
    b ^= 1
print(min(x, y))
