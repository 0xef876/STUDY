# BOJ 11727
import sys
def solution(n):
    dp = [0] * (1001)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    if n == 1 or n == 2:
        return dp[n]
    else:
        for i in range(3,len(dp)):
            dp[i] = dp[i-1] + 2 * dp[i-2]
        return dp[n] % 10007
print(solution(int(sys.stdin.readline().rstrip())))
