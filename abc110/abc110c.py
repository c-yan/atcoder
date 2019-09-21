S = input()
T = input()

d = {}
for i in range(len(S)):
    d[S[i]] = T[i]

t = []
for i in range(len(S)):
    t.append(d[S[i]])

if ''.join(t) != T or len(d.values()) != len(set(d.values())):
    print('No')
else:
    print('Yes')
