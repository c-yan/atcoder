N, *x = map(int, open(0).read().split())

print(sum(abs(a) for a in x))
print(sum(a * a for a in x) ** 0.5)
print(max(abs(a) for a in x))
