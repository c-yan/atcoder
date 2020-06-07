S = input()
A, B, C, D = map(int, input().split())

t = set([A, B, C, D])

result = []
for i in range(len(S)):
    if i in t:
        result.append('"')
    result.append(S[i])
if len(S) in t:
    result.append('"')
print(''.join(result))
