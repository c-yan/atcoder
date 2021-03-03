N, K = map(int, input().split())
wp = [tuple(map(int, input().split())) for _ in range(N)]


def is_ok(n):
    wp.sort(key=lambda x: x[0] * (x[1] - n), reverse=True)
    a = sum(w * p / 100 for w, p in wp[:K])
    b = sum(w for w, _ in wp[:K])
    return (a / b) * 100 >= n


ok = 0.0
ng = 100.1
for i in range(100):
    m = (ok + ng) / 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
