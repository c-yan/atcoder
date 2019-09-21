import sys
n = int(input())
if n == 0:
    print('0')
    sys.exit()
t = []
while n != 0:
    r = n % 2
    t.append(str(r))
    n = (n - r) // -2
print(''.join(t[::-1]))
