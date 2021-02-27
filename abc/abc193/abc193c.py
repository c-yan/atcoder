N = int(input())

s = set()
for i in range(2, int(N ** 0.5) + 1):
    for j in range(2, N + 1):
        t = i ** j
        if t > N:
            break
        s.add(t)
print(N - len(s))
