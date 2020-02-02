N = int(input())
H = list(map(int, input().split()))

for i in range(N - 2, 0, -1):
    if H[i] <= H[i + 1]:
        continue
    H[i] -= 1
    if H[i] > H[i + 1]:
        print('No')
        exit()
print('Yes')
