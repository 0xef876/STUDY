N,K=map(int,input().split())
data = []
for _ in range(N):
    w,v = map(int,input().split())
    data.append([w,v])

data.sort()
dp = [[0]*(K+1) for _ in range(N+1)]

# dp[i][j] = i번째 물건까지 고려했을 때, j무게까지 고려했을 때 최대 가치
for i in range(1,N+1):
    for j in range(1,K+1):
        w = data[i-1][0] # 물건의 무게
        v = data[i-1][1] # 물건의 가치

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j] , v + dp[i-1][j-w])
print(dp[N][K])