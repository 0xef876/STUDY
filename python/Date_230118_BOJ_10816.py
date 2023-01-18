# 10816
M = int(input())
li = list(map(int,input().split()))

N = int(input())
L = list(map(int,input().split()))

dict = {}
for i in range(M):
    try:
        if dict[li[i]]:
            dict[li[i]] += 1
    except:
        dict[li[i]] = 1
    
for j in L:
    try :
        if dict[j]:
            print(dict[j], end =" ")
    except:
        print(0,end=' ')
