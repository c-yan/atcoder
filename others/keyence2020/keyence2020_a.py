H = int(input())
W = int(input())
N = int(input())

t = max(H, W)
print((N + t - 1) // t)
