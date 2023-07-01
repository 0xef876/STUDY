import sys
input = sys.stdin.readline

a = int(input())
data = [tuple(map(int, input().split())) for _ in range(a)]

ans = 0
for i in range(a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            p1,p2,p3 = data[i],data[j],data[k]
            x = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])
            y = (p2[0]-p3[0])*(p2[0]-p3[0]) + (p2[1]-p3[1])*(p2[1]-p3[1])
            z = (p3[0]-p1[0])*(p3[0]-p1[0]) + (p3[1]-p1[1])*(p3[1]-p1[1])
            if 2 * max(x,y,z) == x + y + z:
                ans += 1

print(ans)
