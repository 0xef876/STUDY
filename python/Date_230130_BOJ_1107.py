# BOJ 1107
import sys
import itertools
n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline().rstrip())
curr = 100
case = abs(curr - int(n))

if m != 0:
    user_input =set(map(int,sys.stdin.readline().split()))

    res = {0,1,2,3,4,5,6,7,8,9} - user_input
    res = list(res)
    # print("curr =",curr)
    # print(res)
    ans = abs(curr - int(n))
    for _ in range(len(n)+1,0,-1):
        data = list(itertools.product(res, repeat = _))
        for d in data:
            s = ""
            for i in d:
                s += str(i)
                    # |s - 100|
            # 리모컨 번호 누르고 only + or - 누르는 경우
            case1 = abs(int(n) - int(s)) + len(s)
            # 번호안누르고 , only + or - 누르는 경우
            if int(n) == int(s):
                case2 = abs(int(n) - (curr - int(s))) 
            # 아무것도 안누르고 +, - 만 누르는경우
                ans = min(case1,case2,ans,case)
            else:
                ans = min(case1,case,ans)
    print(ans)
else:
    print(min(case,len(n)))
