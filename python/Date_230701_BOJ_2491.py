n = int(input())
data = list(map(int, input().split()))

ans1 = 0
ans2 = 0
temp = 0
temp2 = 0

for i in range(len(data)-1):
    if data[i] >= data[i+1]:
        temp += 1
    else:
        if ans1 <= temp:
            ans1 = temp
        temp = 0

    if data[i] <= data[i+1]:
        temp2 += 1
    else:
        if ans2 <= temp2:
            ans2 = temp2
        temp2 = 0

if ans1 <= temp:
    ans1 = temp
if ans2 <= temp2:
    ans2 = temp2

print(max(ans1+1, ans2+1))