H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
elif W % 2 == 0:
    print(H * W // 2)
else:
    if H % 2 == 0:
        print(H * W // 2)
    else:
        print((W + 1) // 2 + (H - 1) * W // 2)
