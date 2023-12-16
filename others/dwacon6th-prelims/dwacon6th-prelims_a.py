N = int(input())

total = 0
p = 0
d = {}
for _ in range(N):
    s, t = input().split()
    t = int(t)
    total += t
    d[s] = total
print(total - d[input()])
