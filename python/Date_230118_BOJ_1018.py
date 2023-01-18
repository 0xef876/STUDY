
# 1018
def change(x):
    if x == 'B':
        return 'W'
    else:
        return 'B'

n,m = map(int,input().split())
pan1 = [[0 for i in range(8)] for j in range(8)]
pan2 = [[0 for i in range(8)] for j in range(8)]

for i in range(8):
    if i % 2 == 0:
        pan1[i][0] = 'B'
    else:
        pan1[i][0] = 'W'
for i in range(8):
    if i % 2 == 0:
        pan2[i][0] = 'W'
    else:
        pan2[i][0] = 'B'

for i in pan1:
    prev = i[0]
    for j in range(len(i)):
        i[j] = change(prev)
        prev = i[j]

for i in pan2:
    prev = i[0]
    for j in range(len(i)):
        i[j] = change(prev)
        prev = i[j]

li = []
for i in range(n):
    s = input()
    temp = []
    for _ in s:
        temp.append(_)
    li.append(temp)

ans = 9999999
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0
        for k in range(8):
            for l in range(8):
                if pan1[k][l] != li[k+i][l+j]:
                    count1 += 1
                if pan2[k][l] != li[k+i][l+j]:
                    count2 += 1
        ans = min(ans,count1,count2)
print(ans)
