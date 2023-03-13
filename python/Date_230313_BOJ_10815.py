n = int(input())
data = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))
dic = {}
for i in data:
    dic[i] = 0

for i in data2:
    try:
        if dic[i] == 0:
            print(1,end = " ")
    except:
        print(0, end=" ")
