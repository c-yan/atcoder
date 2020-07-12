N, *a = map(int, open(0).read().split())

print(sum(e % 2 for e in a[::2]))
