N, S = input().split()
N = int(N)

result = 0
t = {}
t[(0, 0)] = 1
a, b = 0, 0
for c in S:
    if c == 'A':
        a += 1
    elif c == 'T':
        a -= 1
    elif c == 'C':
        b += 1
    elif c == 'G':
        b -= 1
    if (a, b) in t:
        result += t[(a, b)]
        t[(a, b)] += 1
    else:
        t[(a, b)] = 1
print(result)
