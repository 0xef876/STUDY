n = int(input())
data = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))