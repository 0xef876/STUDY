# BOJ 2579
import sys
def solution(data):
    if len(data) == 1:
        return [data[0]]
    if len(data) == 2:
        return [max(data[0] + data[1] , data[1])]
    dp = []
    dp.append(data[0])
    dp.append(max(data[0] + data[1] , data[1]))
    dp.append(max(data[0]+data[2],data[1]+data[2]))
    for i in range(3,len(data)):
        dp.append(max(dp[i-2] + data[i] , dp[i-3] + data[i] + data[i - 1]))
    return dp
num = int(sys.stdin.readline().rstrip())
data = []
for i in range(num):
    data.append(int(sys.stdin.readline().rstrip()))
print(solution(data)[-1])
