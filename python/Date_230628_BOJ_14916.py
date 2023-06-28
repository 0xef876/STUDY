n = int(input())
ans = []


for i in range(n//5+1):
    two = 0
    five = 0
    if (n - 5*i) % 2 == 0:
        five = i
        two = (n - 5*i) // 2
        ans.append(five + two)


if len(ans):
    print(min(ans))
else:
    print(-1)