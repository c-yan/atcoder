S = input()
T = input()

if len(S) + 1 == len(T) and S == T[:-1]:
    print('Yes')
else:
    print('No')
