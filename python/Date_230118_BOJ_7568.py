# BOJ _ 7568
import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    li.append((a,b))
ans = []
for i in range(n):
    count = 0 
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            count += 1
    ans.append(count + 1) 
for i in ans:
    print(i,end=' ')
