N = int(input())

c = 1
for i in range(1, 555556):
    t = str(i)
    if len(t) == t.count(t[0]):
        if c == N:
            print(t)
            exit()
        c += 1
