import sys
dp = [0 for i in range(1001)]
dp[1],dp[2] = 1,2
for i in range(3,1001):
    dp[i]=dp[i-1]+dp[i-2]

while True:
    a,b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    cnt = 0
    for i in range(1,1001):
        if dp[i] >= a and dp[i] <= b:
            cnt += 1     
    print(cnt)
