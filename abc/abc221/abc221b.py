S = input()
T = input()

a = []
for i in range(len(S)):
    if S[i] != T[i]:
        a.append(i)

if len(a) == 0 or (len(a) == 2 and a[0] + 1 == a[1] and S[a[0]] == T[a[1]] and S[a[1]] == T[a[0]]):
    print('Yes')
else:
    print('No')
