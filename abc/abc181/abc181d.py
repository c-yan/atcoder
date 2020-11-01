from collections import Counter

S = input()

if len(S) == 1:
    if S == '8':
        print('Yes')
    else:
        print('No')
elif len(S) == 2:
    if ''.join(sorted(S)) in ['16', '24', '23', '04', '48', '56', '46', '27', '08', '88', '69']:
        print('Yes')
    else:
        print('No')
else:
    c = Counter(S)
    for x in range(104, 1000, 8):
        d = Counter(str(x))
        for k in d:
            if k not in c:
                break
            if d[k] > c[k]:
                break
        else:
            print('Yes')
            exit()
    print('No')
