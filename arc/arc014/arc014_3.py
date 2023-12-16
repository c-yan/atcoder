N = int(input())
S = input()

s = set()
for b in S:
    if b in s:
        s.remove(b)
    else:
        s.add(b)
print(len(s))
