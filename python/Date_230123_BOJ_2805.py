# 2805
import sys

a,b = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

s = 0
e = data[-1]

while s <= e:
    cnt = 0 
    mid = (s+e) // 2
    for i in range(a):
        if data[i] > mid:
            cnt += data[i] - mid
    if cnt >= b:
        s = mid + 1
    else:
        e = mid - 1

print(e)
