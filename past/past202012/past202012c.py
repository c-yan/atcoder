N = int(input())

if N == 0:
    print('0')
    exit()

t = ''
while N > 0:
    a = N % 36
    if a < 10:
        t += str(a)
    else:
        t += chr(ord('A') + a - 10)
    N //= 36
print(t[::-1])
