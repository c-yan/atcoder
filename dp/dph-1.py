# 貰うDP
def main():
  divisor = 10 ** 9 + 7
  h, w = map(int, input().split())
  a = [input() for _ in range(h)]
  dp = [[0] * w for _ in range(h)]
  dp[0][0] = 1
  dp0 = dp[0]
  a0 = a[0]
  for j in range(1, w):
    if a0[j] != '#':
      dp0[j] = dp0[j - 1]
  for i in range(1, h):
    dpi = dp[i]
    dpi1 = dp[i - 1]
    ai = a[i]
    if ai[0] != '#':
      dpi[0] = dpi1[0]
    for j in range(1, w):
      if ai[j] != '#':
        dpi[j] = (dpi1[j] + dpi[j - 1]) % divisor
  print(dp[h - 1][w - 1])
main()
