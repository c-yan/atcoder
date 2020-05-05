a, b, c = map(int, input().split())

if c - a - b > 0 and (c - a - b) * (c - a - b) > 4 * a * b:
    print('Yes')
else:
    print('No')
