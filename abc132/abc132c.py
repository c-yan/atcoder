n = int(input())
d = [int(e) for e in input().split()]
d.sort()
print(d[n // 2] - d[n // 2 - 1])
