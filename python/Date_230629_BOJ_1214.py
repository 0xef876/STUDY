import sys
total,curr1,curr2 = map(int,sys.stdin.readline().split())

if curr1 > curr2:
    curr1,curr2 = curr2,curr1

n = total // curr2 + 1
ans = curr2 * n

for i in range(n-1,-1,-1):
    div = (total - curr2 * i) // curr1
    mod = (total - curr2 * i) % curr1
    if mod == 0:
        print(total)
        exit()
    ans2 = (curr1 * (div + 1)) + curr2 * i
    if ans == ans2: # 최소비용이 계속 반복된다면, 더이상 계산할 필요가 없다.
        break
    ans = min(ans,ans2)
print(ans)