n = int(input())
ans = 0
for i in range(1,n+1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        ans += 1
    else:
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            ans += 1    

print(ans)