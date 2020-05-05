N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [None] * (K + 1)
dp[0] = False  # 手番が回ってきた時に0個の場合は必ず負け
for i in range(1, K + 1):
    # 手番を回して、相手が負けのものが一つでもあれば勝ち
    dp[i] = any(not dp[i - x] for x in a if x <= i)

if dp[K]:
    print('First')
else:
    print('Second')
