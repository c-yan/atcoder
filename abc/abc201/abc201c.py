from itertools import product, permutations

S = input()

if S.count('o') > 4 or S.count('x') == 10:
    print(0)
    exit()

base = []
option = []
for i in range(10):
    if S[i] == 'o':
        base.append(str(i))
    if S[i] != 'x':
        option.append(str(i))

result = set()
for p1 in product(option, repeat=4 - len(base)):
    for p2 in permutations(base + list(p1)):
        result.add(''.join(list(p2)))
print(len(result))
