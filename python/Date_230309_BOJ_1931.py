import sys
n =int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    data.append((s,e))

data.sort(key = lambda x : (x[1],x[0]))
count = 1
temp = data[0]
# print(data)
for i in range(1,len(data)):
    if data[i][0] >= temp[1]:
        count += 1
        temp = data[i]
print(count)
