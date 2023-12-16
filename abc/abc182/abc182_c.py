N = input()

t = [int(c % 3) for c in N]
x = sum(t)

if x % 3 == 0:
    print(0)
elif x % 3 == 1:
    if 1 in t:
        print(1)
    else:
        print(2)
elif x % 3 == 2:
    if 2 in t:
        print(1)
    else:
        print(2)
