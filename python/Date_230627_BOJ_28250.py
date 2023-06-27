n = int(input())
a = [0, 0, 0]
data = list(map(int,input().split()))
for i in range(n):
    x = data[i]
    if x < 2:
        a[x] += 1
    else:
        a[2] += 1
result = 2 * a[0] * a[1] + a[0] * (a[0] - 1) // 2 + a[0] * a[2]
print(result)
