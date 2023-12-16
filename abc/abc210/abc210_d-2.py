from sys import stdin

readline = stdin.readline

H, W, C = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(H)]

result = A[0][0] + A[0][1] + C
m = min(min(a) for a in A)
for i in range(H):
    for j in range(W):
        for d in range(1, 10 ** 6):
            t = A[i][j] + C * d
            if t + m > result:
                break
            for k in range(d + 1):
                if i + k >= H:
                    break
                l = d - k
                if j + l < W:
                    result = min(result, t + A[i + k][j + l])
                if j - l >= 0:
                    result = min(result, t + A[i + k][j - l])
print(result)
