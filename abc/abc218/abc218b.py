P = map(int, open(0).read().split())

print(*(chr(ord('a') + p - 1) for p in P), sep='')
