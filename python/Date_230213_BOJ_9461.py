import sys
def solution(n):
    dp = [0] * (101)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    
    if n <=5:
        return dp[n]
    else:
        for i in range(6,len(dp)):
            dp[i] = dp[i-3] + dp[i-2]
        return dp[n]


Val = int(sys.stdin.readline().rstrip())
for i in range(Val):
    print(solution(int(sys.stdin.readline().rstrip())))
