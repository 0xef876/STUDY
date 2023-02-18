import sys
n,m = map(int,sys.stdin.readline().split())

def f(val):
    ans = 1
    for i in range(1,val+1):
        ans *= i
    return ans

nCm = f(n) // (f(abs(n-m)) * f(m))
print(nCm)
