from sys import exit

N = int(input())

if N == 0:
    print('0')
    exit()

t = []
while N != 0:
    r = N % 2
    t.append(str(r))
    n = (N - r) // -2
print(''.join(t[::-1]))
