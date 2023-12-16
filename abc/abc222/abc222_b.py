N, P, *a = map(int, open(0).read().split())

print(len([a for x in a if x < P]))
