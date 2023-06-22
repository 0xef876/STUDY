n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])
print(max(dp))