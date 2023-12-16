S = input()
T = input()

for i in range(len(S)):
    a = S[i]
    b = T[i]
    if a != b:
        if a == '@' and b in 'atcoder':
            a = b
        if b == '@' and a in 'atcoder':
            b = a
    if a != b:
        print('You will lose')
        break
else:
    print('You can win')
