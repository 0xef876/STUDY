n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

dp[0][0] = data[0][0]
for i in range(1,len(data)):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + data[i][j]

print(max(dp[n-1]))