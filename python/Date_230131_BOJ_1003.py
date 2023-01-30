# BOJ 1003
import sys
zero = [1,0,1]
one = [0,1,1]
def solve(x):
    n = len(zero)
    if x >= n:
        for i in range(n,x+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[x], one[x])
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    testcase = int(sys.stdin.readline().rstrip())
    solve(testcase)
