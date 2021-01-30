A, B, C = map(int, input().split())

if C == 0:
    if B >= A:
        print('Aoki')
    else:
        print('Takahashi ')
elif C == 1:
    if A >= B:
        print('Takahashi ')
    else:
        print('Aoki')
