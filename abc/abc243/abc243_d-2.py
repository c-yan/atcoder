N, X = map(int, input().split())
S = input()

a = list(bin(X))[2:]
for c in S:
    if c == 'U':
        a.pop()
    elif c == 'L':
        a.append('0')
    elif c == 'R':
        a.append('1')
print(int(''.join(a), 2))
