N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            print('Yes')
            exit()
print('No')
