N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
print(sum(p[:K]))
