#2108
import sys,math

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

san = round(sum(li) / len(li))
if san == 0:
    san = math.ceil(sum(li) / len(li))
li.sort()
jung = li[len(li) // 2]
dict = {}
for i in li:
    try :
        if dict[i]:
            dict[i] += 1
    except:
        dict[i] = 1 
temp = []
for i in dict:
    if dict[i] == max(dict.values()):
        temp.append((i,dict[i]))
temp.sort()
if len(temp) == 1:
    choi = temp[0][0]
else:
    choi = temp[1][0]
ran = max(li) - min(li)
print(int(san))
print(jung)
print(choi)
print(ran)
