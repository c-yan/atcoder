N = int(input())

c = 1
for i in range(1, 10):
    for j in range(1, 10):
        if c != N:
            c += 1
            continue
        print(str(j) * i)
        exit()
