
# 1874
import sys
# push : + , pop : 
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

ans = []
ans_list = []
res = []
idx = 0
val = 1
while val != n+1:
    try:
        if  res[-1] == data[idx]:
            a = res.pop() # pop
            ans.append(a)
            ans_list.append('-')
            idx += 1
        else: 
            res.append(val)
            ans_list.append('+')
            val += 1 
    except:
        res.append(val)
        ans_list.append('+')

        val += 1
while len(res) != 0:
    ans.append(res.pop())
    ans_list.append('-')
if data != ans:
    print("NO")
else:
    for i in ans_list:
        print(i)
