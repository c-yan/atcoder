S = input()

t = list(sorted(list(set(chr(i) for i in range(ord('a'), ord('z') + 1)) - set(S))))
if len(t) == 0:
    print('None')
else:
    print(t[0])
