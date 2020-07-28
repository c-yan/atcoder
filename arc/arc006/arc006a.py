E = set(input().split())
B = input()
L = set(input().split())

t = E & L
if len(t) == 6:
    print(1)
elif len(t) == 5:
    if B in L:
        print(2)
    else:
        print(3)
elif len(t) == 4:
    print(4)
elif len(t) == 3:
    print(5)
else:
    print(0)
