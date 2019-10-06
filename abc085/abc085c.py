from sys import exit

N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1 - i):
        k = N - i - j
        if 10000 * i + 5000 * j + 1000 * k == Y:
            print('%d %d %d' % (i, j, k))
            exit()
print('-1 -1 -1')
