import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]


# DP
# dp[i][j][k] : (i,j)에 k방향으로 놓여있는 경우의 수
# k = 0 : 가로, k = 1 : 세로, k = 2 : 대각선
dp = [[0, 0, 0] for _ in range(n)]
dp[0][1][0] = 1 # 시작점

for i in range(n):
    for j in range(2, n):
        if data[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if data[i-1][j] == 0 and data[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
                
print(sum(dp[n-1][n-1]))
