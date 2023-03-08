n = int(input())
data = list(map(int,input().split()))
new_data = set(data)
new_data = list(new_data)
new_data = sorted(new_data)

dic = {}
for i in range(len(new_data)):
    try: 
        if dic[new_data[i]] != None:
            continue
    except:
        dic[new_data[i]] = i
        
for i in data:
    print(dic[i],end = ' ')
