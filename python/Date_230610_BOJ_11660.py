import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = []
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + data[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
