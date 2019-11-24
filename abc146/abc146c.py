A, B, X = map(int, input().split())


def is_ok(N):
    return A * N + B * len(str(N)) > X


l = 0
r = 1000000001
while r > l+1:
    m = l + (r - l) // 2
    if is_ok(m):
        r = m
    else:
        l = m
print(l)
