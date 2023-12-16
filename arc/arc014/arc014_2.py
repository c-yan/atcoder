N = int(input())
W = [input() for _ in range(N)]

used = set([W[0]])
prev = W[0]
for i in range(1, N):
    w = W[i]
    if w in used:
        break
    used.add(w)
    if prev[-1] != w[0]:
        break
    prev = w
else:
    i = -1

if i == -1:
    print('DRAW')
elif i % 2 == 0:
    print('WIN')
elif i % 2 == 1:
    print('LOSE')
