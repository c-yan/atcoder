from collections import Counter

S = input()

c = Counter(S)
a = 0
b = 0
for k in c:
    a += c[k] // 2
    b += c[k] % 2

if b == 0:
    print(len(S))
else:
    print((a // b) * 2 + 1)
