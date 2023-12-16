from itertools import combinations

N, *L = map(int, open(0).read().split())

result = 0
for a, b, c in combinations(L, 3):
    if a == b or b == c or c == a:
        continue
    if a + b > c and b + c > a and c + a > b:
        result += 1
print(result)
