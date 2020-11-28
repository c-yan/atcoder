N, A, B = map(int, open(0).read().split())

if N <= A:
    print('Takahashi')
else:
    if A > B:
        print('Takahashi')
    elif A < B:
        print('Aoki')
    else:
        if N % (A + 1) == 0:
            print('Aoki')
        else:
            print('Takahashi')
