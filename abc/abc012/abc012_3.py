N = int(input())

t = 2025 - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == t:
            print('%d x %d' % (i, j))
