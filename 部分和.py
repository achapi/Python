#aが配列でsが和
def partialsum(a,s):
  m = [0] + a
  n = len(m)
  dp = [[0 for i in range(s+1)] for n in range(n)]
  dp[0][0] = 1
  for i in range(1,n):
    for j in range(s+1):
      if j >= m[i]:dp[i][j] = dp[i-1][j-m[i]] or dp[i-1][j]
      else:dp[i][j] = dp[i-1][j]
  return dp[-1][-1]