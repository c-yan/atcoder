a, b, c = map(int, input().split())

x = [a, b, c]
x.sort()

if x[0] == x[1]:
    print(x[2])
elif x[1] == x[2]:
    print(x[0])
else:
    print(0)
