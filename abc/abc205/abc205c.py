A, B, C = map(int, input().split())

C = C % 2 + 2

if pow(A, C) < pow(B, C):
    print('<')
elif pow(A, C) > pow(B, C):
    print('>')
elif pow(A, C) == pow(B, C):
    print('=')
