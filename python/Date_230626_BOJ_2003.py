N,S = map(int,input().split())
data = list(map(int,input().split()))

# 투포인터
start = 0
end = 0
sum = 0
ans = 0
while True:
    if sum == S:
        sum -= data[start]
        start += 1
        ans += 1
    elif sum > S:
        sum -= data[start]
        start += 1
    elif end == N:
        break
    else:
        sum += data[end]
        end += 1

print(ans)
    
