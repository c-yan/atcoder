N = int(input())
s = input()

t = ''
for c in s:
    t += c
    while t[-3:] == 'fox':
        t = t[:-3]
print(len(t))
