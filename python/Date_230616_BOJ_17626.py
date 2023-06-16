import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = i
    for j in range(1,i):
        if j*j > i:
            break
        dp[i] = min(dp[i],dp[i-j*j]+1)

print(dp[n])