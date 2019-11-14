n = int(input())
a = list(map(int, input().split()))

a.sort()
x = a[-1]
b = [(min(e, x - e), e) for e in a[:-1]]
b.sort()
print(x, b[-1][1])
