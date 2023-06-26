N,S = map(int,input().split())
data = list(map(int,input().split()))

# 투포인터
start = 0
end = 0
sum = 0
ans = 100000000
while True:
    if sum >= S:
        sum -= data[start]
        start += 1
        ans = min(ans,end-start+1)
    elif end == N:
        break
    else:
        sum += data[end]
        end += 1

if ans == 100000000:
    print(0)
else:
    print(ans)
    
