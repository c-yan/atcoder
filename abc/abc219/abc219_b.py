S = {}
S[1] = input()
S[2] = input()
S[3] = input()
T = input()

print(''.join(S[int(c)] for c in T))
