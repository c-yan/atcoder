from sys import exit

S = input()[::-1]

while True:
    if S == '':
        print('YES')
        exit()
    for w in ['maerd', 'remaerd', 'esare', 'resare']:
        if S.startswith(w):
            S = S[len(w):]
            break
    else:
        print('NO')
        exit()
