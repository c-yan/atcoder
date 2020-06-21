N = int(input())

t = []
while N > 0:
    N -= 1
    t.append(chr(N % 26 + ord('a')))
    N //= 26
print(''.join(t[::-1]))
