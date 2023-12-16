S = input()
T = input()

S += S
if S.find(T) != -1:
    print('Yes')
else:
    print('No')
