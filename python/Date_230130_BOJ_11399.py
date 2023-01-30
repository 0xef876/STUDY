# BOJ 11399
import sys
n = int(sys.stdin.readline().rstrip())
data =list(map(int,sys.stdin.readline().split()))
ans = 0
res = 0
def solve(L,idx):
    global ans,res
    if len(L) == idx:
        return res
    ans += L[idx]
    idx += 1
    res += ans
    return solve(L,idx)

data.sort()
print(solve(data,0))
