import sys
n = int(sys.stdin.readline().rstrip())

def solve(val):
    if val <= 3:
        dp = [1,2,4]
        return dp[val - 1]
    elif val > 3:
        dp = [1,2,4] + [0] * (val-3)
        for i in range(3,val):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[-1]
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    print(solve(num))
