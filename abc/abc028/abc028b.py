S = input()

d = {}
for c in 'ABCDEF':
    d[c] = 0

for c in S:
    d[c] += 1

print(*(d[c] for c in 'ABCDEF'))
