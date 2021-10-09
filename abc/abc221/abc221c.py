from itertools import product

N = input()

result = 0
for p in product(range(2), repeat=len(N)):
    a = [[], []]
    for i in range(len(N)):
        a[p[i]].append(N[i])
    if len(a[0]) == 0 or len(a[1]) == 0:
        continue
    a[0].sort(reverse=True)
    a[1].sort(reverse=True)
    result = max(result, int(''.join(a[0])) * int(''.join(a[1])))
print(result)
