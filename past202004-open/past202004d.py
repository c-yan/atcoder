from itertools import product
from re import search

S = input()

cs = set(S)
cs.add('.')

result = 0
for i in range(1, 4):
    for p in product(cs, repeat=i):
        if search(''.join(p), S):
            result += 1
print(result)
