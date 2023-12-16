H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    print(((H + 1) // 2) * ((W + 1) // 2))
