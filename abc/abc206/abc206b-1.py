N = int(input())

c = 0
for i in range(1, 10 ** 9):
    c += i
    if c < N:
        continue
    print(i)
    break
