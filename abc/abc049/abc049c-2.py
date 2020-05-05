S = input()

ts = ['']
while True:
    nts = []
    for t in ts:
        for w in ['dreamer', 'eraser', 'dream', 'erase']:
            tw = t + w
            if S == tw:
                print('YES')
                exit()
            if S.startswith(tw):
                nts.append(tw)
    if len(nts) == 0:
        print('NO')
        exit()
    ts = nts
