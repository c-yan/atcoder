H, W = map(int, input().split())
h, w = map(int, input().split())

print(H * W - (h * W + w * H - h * w))
