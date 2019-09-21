def main():
  s = input()
  divisor = 10 ** 9 + 7
  dp = [[0] * 13 for _ in range(len(s) + 1)]
  dp[0][0] = 1
  lut = [i % 13 for i in range(130)]
  list10 = list(range(10))
  list13 = list(range(13))
  for i in range(len(s)):
    dpi = dp[i]
    dpi1 = dp[i + 1]
    if s[i] == '?':
      j10 = 0
      for j in list13:
        dpij = dpi[j]
        for k in list10:
          dpi1[lut[j10 + k]] += dpij
        j10 += 10
    else:
      t = int(s[i])
      for j in list13:
        dpi1[t] += dpi[j]
        t = lut[t + 10]
    for k in list13:
      dpi1[k] %= divisor
  print(dp[len(s)][5])
main()
