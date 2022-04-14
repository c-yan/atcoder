A, B, C, D = map(int, input().split())

if A * 3600 + B * 60 < C * 3600 + D * 60 + 1:
    print('Takahashi')
else:
    print('Aoki')
