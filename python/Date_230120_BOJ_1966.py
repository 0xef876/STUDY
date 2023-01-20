
# 1966
import sys
n = int(sys.stdin.readline())
def change_idx(i,L):
    if i == 0:
        return L-1
    else:
        i -= 1
        return i
for _ in range(n):
    count = 0
    N,M = map(int,input().split())
    temp = list(map(int,input().split()))
    idx = M
    while True:
        if max(temp) == temp[0]:
            if idx == 0:
                count += 1
                print(count)
                break
            else:
                temp.pop(0)
                idx = change_idx(idx,len(temp))
                count += 1
        else:
            temp.append(temp.pop(0))
            idx = change_idx(idx,len(temp))
