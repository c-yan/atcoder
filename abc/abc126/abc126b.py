def mmok(i):
    return 1 <= i <= 12


S = input()
h = int(S[:2])
l = int(S[2:])

if mmok(h):
    if mmok(l):
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if mmok(l):
        print('YYMM')
    else:
        print('NA')
