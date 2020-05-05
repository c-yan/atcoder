N = int(input())

prev = input()
used = set([prev])
for _ in range(N - 1):
    s = input()
    if s in used or prev[-1] != s[0]:
        print('No')
        exit()
    prev = s
    used.add(s)
print('Yes')
