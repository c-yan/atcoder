S = input()

a = {S}
for i in range(1, len(S)):
    a.add(S[i:] + S[:i])
    a.add(S[:-i] + S[-i:])
a = sorted(a)
print(a[0])
print(a[-1])
