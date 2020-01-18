N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

t = [(x + l, x - l) for x, l in XL]
t.sort()
max_r = -float('inf')
result = 0
for i in range(N):
    r, l = t[i]
    if max_r <= l:
        result += 1
        max_r = r
print(result)
