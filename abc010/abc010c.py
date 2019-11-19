from sys import exit
from math import sqrt

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    t = sqrt((txa - x) * (txa - x) + (tya - y) * (tya - y))
    t += sqrt((txb - x) * (txb - x) + (tyb - y) * (tyb - y))
    if t <= T * V:
        print('YES')
        exit()
print('NO')
