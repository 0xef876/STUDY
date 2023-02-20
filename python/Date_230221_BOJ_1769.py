import sys
n = sys.stdin.readline().rstrip()
ans = 0
if n in ['3','6','9']:
        print(0)
        print("YES")
elif len(n) == 1:
     print(0)
     print("NO")
else:
     
    while True:
        
        temp = 0
        for i in n:
            temp += int(i)
        if len(str(temp)) >= 2:
            n = str(temp)
            ans += 1
        elif len(str(temp)) == 1:
            ans += 1
            print(ans)
            if temp in [3,6,9]:
                print('YES')
            else:
                print('NO')
            break
