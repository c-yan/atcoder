N, *a = map(int, open(0).read().split())

print(sum(1 for e in a[::2] if e % 2 == 1))
