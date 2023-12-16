X, N = map(int, input().split())
p = list(map(int, input().split()))

p = set(p)
for i in range(200):
    if X - i not in p:
        print(X - i)
        break
    if X + i not in p:
        print(X + i)
        break
