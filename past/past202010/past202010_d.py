import re

N = int(input())
S = input()

s = re.sub('#+', '#', S)
t = s.split('#')

min_x = t[0]
min_y = t[-1]
c = max(t[1:-1])
c = max(c, min_x + min_y)
print(min_x, c - min_x)
