# BOJ 9375

import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    dic = {}
    x = int(sys.stdin.readline().rstrip())
    for __ in range(x):
        temp = sys.stdin.readline().split()
        try :
            if dic[temp[1]]:
                dic[temp[1]] += 1
        except:
            dic[temp[1]] = 1

    ans = 1
    for i in dic.values():
        ans *= i+1
    
    ans -= 1
    print(ans)
