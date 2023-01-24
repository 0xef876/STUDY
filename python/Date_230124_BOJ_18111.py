# 18111
import sys
a,b,c = map(int,sys.stdin.readline().split())
data = []
for i in range(a):
    temp = list(map(int,sys.stdin.readline().split()))
    data.append(temp) 
time, h = sys.maxsize, 0
for i in range(257):
    m = 0
    M = 0
    for j in range(a):
        for k in range(b):
            if data[j][k] >= i:
                M += data[j][k] - i
            else:
                m += i - data[j][k]
    if m > M + c:
        continue
    t = m + M * 2
    if t <= time:
        time = t
        h = i
print(time,h)
