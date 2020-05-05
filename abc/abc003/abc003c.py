N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

C = 0
for r in R[-K:]:
    C = (C + r) / 2
print(C)
