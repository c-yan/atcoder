S = {}
S['A'] = input()
S['B'] = input()
S['C'] = input()

turn = 'A'
while True:
    if S[turn] == '':
        print(turn)
        break
    t = S[turn][0].upper()
    S[turn] = S[turn][1:]
    turn = t
