from sys import exit

N = int(input())

pt, px, py = 0, 0, 0
for _ in range(N):
    t, x, y = map(int, input().split())
    duration = t - pt
    distance = abs(px - x) + abs(py - y)
    if (distance > duration) or ((duration - distance) % 2 == 1):
        print('No')
        exit()
    pt, px, py = t, x, y
print('Yes')
