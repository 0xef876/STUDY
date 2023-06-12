T = int(input())
for _ in range(T):
    n = int(input())        
    data = []
    data.append(list(map(int,input().split())))    
    data.append(list(map(int,input().split())))
    if n == 1:
        print(max(data[0][0],data[1][0]))
        continue
    
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    dp[0][1] = dp[1][0] + data[0][1]
    dp[1][1] = dp[0][0] + data[1][1]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + data[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + data[1][i]

    print(max(dp[0][n-1],dp[1][n-1]))
