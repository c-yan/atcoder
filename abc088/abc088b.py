n = int(raw_input())
a = [int(e) for e in raw_input().split()]
a.sort()
a.reverse()
print sum(a[::2]) - sum(a[1::2])
