H, W, *A = map(int, open(0).read().split())

print(sum(A) - min(A) * H * W)
