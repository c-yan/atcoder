from sys import exit

N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())

if N in [NG1, NG2, NG3]:
    print('NO')
    exit()

c = 0
while N > 0:
    if N >= 3 and N - 3 not in [NG1, NG2, NG3]:
        N -= 3
        c += 1
    elif N >= 2 and N - 2 not in [NG1, NG2, NG3]:
        N -= 2
        c += 1
    elif N >= 1 and N - 1 not in [NG1, NG2, NG3]:
        N -= 1
        c += 1
    else:
        print('NO')
        exit()
if c <= 100:
    print('YES')
else:
    print('NO')
