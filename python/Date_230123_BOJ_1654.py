# 1654
import sys

a,b = map(int,sys.stdin.readline().split())
data = []
for i in range(a):
    data.append(int(sys.stdin.readline()))

data.sort()

s = 1
e = data[-1]

while s <= e:
    cnt = 0 
    mid = (s+e) // 2
    for i in range(a):
        cnt += data[i] // mid
    if cnt >= b:
        s = mid + 1
    else:
        e = mid - 1

print(e)
