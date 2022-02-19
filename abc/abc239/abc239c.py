x1, y1, x2, y2 = map(int, input().split())

def dist(x1, x2, y1, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

if dist(x1, x2, y1, y2) <= 100:
    l = min(x1, x2) - 5
    r = max(x1, x2) + 5
    t = min(y1, y2) - 5
    d = max(y1, y2) + 5
    for y in range(t, d + 1):
        for x in range(l, r + 1):
            if dist(x, x1, y, y1) == 5 and dist(x, x2, y, y2) == 5:
                print('Yes')
                exit()
print('No')
