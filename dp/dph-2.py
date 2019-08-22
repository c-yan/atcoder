# 配るDP
def main():
  divisor = 10 ** 9 + 7
  h, w = map(int, input().split())
  a = [input() for _ in range(h)]
  dp = [[0] * w for _ in range(h)]
  dp[0][0] = 1
  for i in range(h):
    ai = a[i]    
    dpi = dp[i]    
    if i + 1 < h:
      ai1 = a[i + 1]
      dpi1 = dp[i + 1]
    for j in range(w):
      if j + 1 < w and ai[j + 1] != '#':
        dpi[j + 1] = (dpi[j + 1] + dpi[j]) % divisor
      if i + 1 < h and ai1[j] != '#':
        dpi1[j] = dpi[j]
  print(dp[h - 1][w - 1])
main()
