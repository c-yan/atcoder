N = int(input())
S = input()

result = ''
s = set()
for c in S[::-1]:
    if c in s:
        continue
    result = c + result
    s.add(c)
print(result)
