from sys import exit

M = int(input())
AB = [list(map(int, input().split())) for _ in range(M)]

t = 0
AB.sort(key=lambda x: x[1])
for A, B in AB:
    t += A
    if t > B:
        print('No')
        exit()
print('Yes')
