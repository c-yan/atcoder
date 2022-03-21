N, X = map(int, input().split())
S = input()

q = []
for c in S:
    if c == 'U' and len(q) != 0 and q[-1] != 'U':
        q.pop()
    else:
        q.append(c)

for c in q:
    if c == 'U':
        X >>= 1
    elif c == 'L':
        X <<= 1
    elif c == 'R':
        X <<= 1
        X += 1
print(X)
