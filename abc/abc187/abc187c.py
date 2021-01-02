N = int(input())
S = [input() for _ in range(N)]

t = set()
for s in S:
    if s[0] == '!':
        if s[1:] in t:
            print(s[1:])
            break
        t.add(s)
    else:
        if '!' + s in t:
            print(s)
            break
        t.add(s)
else:
    print('satisfiable')
