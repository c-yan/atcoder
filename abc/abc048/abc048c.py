N, x = map(int, input().split())
a = list(map(int, input().split()))

result = 0
# a[0] が x 以下でないと、a[1] を空にしても条件を満たせない
t = a[0] - x
if t > 0:
    result += t
    a[0] -= t
for i in range(1, N):
    # 箱に入っているキャンディの数が食べれる上限
    t = min(a[i - 1] + a[i] - x, a[i])
    if t > 0:
        result += t
        a[i] -= t
print(result)
