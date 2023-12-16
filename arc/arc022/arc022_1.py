S = input().lower()

t = S.find('i')
if t == -1:
    print('NO')
    exit()

t = S.find('c', t)
if t == -1:
    print('NO')
    exit()

t = S.find('t', t)
if t == -1:
    print('NO')
else:
    print('YES')
