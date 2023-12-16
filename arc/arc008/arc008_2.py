from collections import Counter

N, M = map(int, input().split())
name = input()
kit = input()

nc = Counter(name)
kc = Counter(kit)

result = 0
for c in name:
    if c not in kc:
        result = -1
        break
    result = max(result, (nc[c] + kc[c] - 1) // kc[c])
print(result)
