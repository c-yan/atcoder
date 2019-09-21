N = int(input())
a = list(map(int, input().split()))
y = sum(a) / N
if y < 0:
    y = int(y - 0.5)
else:
    y = int(y + 0.5)
print(sum((x - y) * (x - y) for x in a))
