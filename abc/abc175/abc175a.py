S = input()

t = 0
result = 0
for c in S:
    if c == 'R':
        t += 1
    else:
        t = 0
    result = max(result, t)
print(result)
