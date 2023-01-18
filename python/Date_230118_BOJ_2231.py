# 2231
n = int(input())

m = n
state =False
for i in range(1,n):
    temp = 0
    for j in str(i):
        temp += int(j)
   
    if temp + i == n :
        if m > i:
            m = i
            state = True
if state:
    print(m)
else:
    print(0)
