N, D, H = map(int, input().split())
dh = [tuple(map(int, input().split())) for _ in range(N)]

print(max(max(h - (H - h) / (D - d) * d for d, h in dh), 0))
