# 2775
def check(a,b):
    li = []
    temp = []
    for i in range(b):
        temp.append(i+1)
    li.append(temp)
    
    for i in range(a):
        temp = []
        temp.clear()
        s = 0
        for j in range(len(li[i])):
            s += li[i][j]
            temp.append(s)
        li.append(temp)
    return li[a][b-1]
num = int(input())
for i in range(num):
    k = int(input())
    n = int(input())
    print(check(k,n))
