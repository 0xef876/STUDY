n = input()
n = n.replace('9','6')
dic = {}
for i in n:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
if '6' in dic:
    if dic['6'] % 2 == 0:
        dic['6'] //= 2
    else:
        dic['6'] = dic['6'] // 2 + 1

a = max(dic.values())
print(a)