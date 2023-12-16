S = input().split()
T = input().split()

if sorted(S) != sorted(T):
    print('No')
    exit()

c = 0
for i in range(3):
    if S[i] != T[i]:
        c += 1

if c == 0:
    print('Yes')
elif c == 2:
    print('No')
elif c == 3:
    print('Yes')
