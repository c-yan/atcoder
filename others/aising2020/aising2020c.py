N = int(input())

t = [0] * (10 ** 4 + 1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            n = x * x + y * y + z * z + x * y + y * z + z * x
            if n <= 10 ** 4:
                t[n] += 1

print(*[t[i] for i in range(1, N + 1)], sep='\n')
