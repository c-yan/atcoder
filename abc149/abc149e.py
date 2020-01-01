N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
LB = A[-1] * 2  # 一回の握手で上がる幸福度の下限は、左手も右手もパワーが一番低い人を握った場合
UB = A[0] * 2   # 一回の握手で上がる幸福度の上限は、左手も右手もパワーが一番高い人を握った場合

# cgs[i] は パワーがi以上のゲストの数
cgs = [0] * (UB + 1)
for a in A:
    cgs[a] += 1
for i in range(UB, 0, -1):
    cgs[i - 1] += cgs[i]


# 組み合わせの数がM以上になる一回で発生する幸福度の閾値を二分探索する
def is_ok(n):
    m = 0
    for a in A:
        m += cgs[max(n - a, 0)]
    return m >= M


ok = LB
ng = UB + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

# cps[i] は A[0]～A[i] の累積和
cps = A[:]
for i in range(1, N):
    cps[i] += cps[i - 1]

result = 0
for a in A:
    t = cgs[max(ok - a, 0)]
    if t != 0:
        result += a * t + cps[t - 1]
        M -= t
result += ok * M
print(result)
