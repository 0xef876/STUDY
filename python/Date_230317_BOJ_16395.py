a,b = map(int,input().split())

dp = [[1]*i for i in range(1, a+1)]
for i in range(2, a):
  for j in range(1,i): 
    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

print(dp[a-1][b-1])
