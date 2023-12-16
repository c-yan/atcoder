N = int(input())
a = list(map(int, input().split()))

t = [0] * 8
over = 0
for x in a:
    if x >= 3200:
        over += 1
    else:
        t[x // 400] = 1
print(*[max(sum(t), 0 if over == 0 else 1), sum(t) + over])
