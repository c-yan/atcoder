A, B, C = map(int, input().split())

C = (C + 1) % 2 + 1

if pow(A, C) < pow(B, C):
    print('<')
elif pow(A, C) > pow(B, C):
    print('>')
elif pow(A, C) == pow(B, C):
    print('=')
