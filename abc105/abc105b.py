from sys import exit

N = int(input())

for i in range(N // 7 + 1):
    if (N - 7 * i) % 4 != 0:
        continue
    print('Yes')
    exit()
print('No')
