N, *A = map(int, open(0).read().split())

P = 0
cells = [0] * 4
for a in A:
    cells[0] = 1
    for i in range(3, -1, -1):
        if cells[i] == 0:
            continue
        if i + a >= 4:
            P += 1
            cells[i] = 0
        else:
            cells[i + a] = 1
            cells[i] = 0
print(P)
