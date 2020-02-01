N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort()
print(sum(l[-K:]))
