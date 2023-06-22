n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = a[0]
for i in range(1,n):
    dp[i] = max(dp[i - 1] + a[i], a[i])
print(max(dp))