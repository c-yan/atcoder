import sys
n = int(input())
h = [int(e) for e in input().split()]
for i in range(n - 2, 0, -1):
    if h[i] > h[i + 1]:
        h[i] -= 1
    if h[i] > h[i + 1]:
        print('No')
        sys.exit()
print('Yes')
