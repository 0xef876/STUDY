n,k = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
for i in data:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])
