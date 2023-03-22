a,b = map(int,input().split())
c = [[0 for i in range(b)] for j in range(a)]

prefix_sum = [[0] * (b+1) for _ in range(a+1)]

for i in range(a):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        c[i][j] = data[j]

                     
d = int(input())

for i in range(1, a + 1):
    for j in range(1, b + 1):
        prefix_sum[i][j] = c[i - 1][j - 1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i -1][j - 1]

for i in range(d):
    x1,y1,x2,y2 = map(int,input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])
