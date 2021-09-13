N = int(input())

a = []
while N != 0:
    if N % 2 == 0:
        a.append('B')
        N //= 2
    else:
        a.append('A')
        N -= 1
print(*reversed(a), sep='')
