S = input()

S = S[::-1]
candidates = [s[::-1] for s in ['dream', 'dreamer', 'erase', 'eraser']]

i = 0
while i < len(S):
    for c in candidates:
        if S.startswith(c, i):
            i += len(c)
            break
    else:
        print('NO')
        exit()
print('YES')
