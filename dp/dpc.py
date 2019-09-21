n = int(input())
d = [[int(e) for e in input().split()] for i in range(n)]
f = [None for i in range(n)]
f[0] = d[0]
for i in range(1, n):
    f[i] = [max(f[i - 1][1] + d[i][0], f[i - 1][2] + d[i][0]), max(f[i - 1][0] + d[i]
                                                                   [1], f[i - 1][2] + d[i][1]), max(f[i - 1][0] + d[i][2], f[i - 1][1] + d[i][2])]
print(max(f[n - 1]))
