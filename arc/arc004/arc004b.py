N, *d = map(int, open(0).read().split())

print(sum(d))
print(max(0, 2 * max(d) - sum(d)))
