# BOJ 11659

import sys

a,b = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

dp = [0] * (a+1)
dp[0] = 0
dp[1] = data[0]
for i in range(2,a+1):
    dp[i] = dp[i-1] + data[i-1]
for i in range(b):
    data = list(map(int,sys.stdin.readline().split()))
    print(dp[data[1]] - dp[data[0]-1])
