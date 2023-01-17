# BOJ 11650
def solution():
    li =  []
    N = int(input())
    for i in range(N):
        a,b = map(int,input().split())
        li.append([a,b])
    ans = sorted(li,key=lambda x : (x[0],x[1]))

    return ans

for i in solution():
    for j in i:
        print(j,end=' ')
    print()