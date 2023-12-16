N = int(input())

R = 0
B = 0
for _ in range(N):
    S = input()
    R += S.count('R')
    B += S.count('B')

if R == B:
    print('DRAW')
elif R > B:
    print('TAKAHASHI')
elif B > R:
    print('AOKI')
