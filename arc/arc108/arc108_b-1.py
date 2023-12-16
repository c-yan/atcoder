N = int(input())
s = input()

t = [None] * len(s)
r = 0
for c in s:
    t[r] = c
    r += 1
    while r >= 3 and t[r - 1] == 'x' and t[r - 2] == 'o' and t[r - 3] == 'f':
        r -= 3
print(r)
