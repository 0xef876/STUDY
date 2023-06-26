N= int(input())

# 에라토스테네스의 체
prime = [True] * (N+1)
for i in range(2,int(N**0.5)+1):
    if prime[i]:
        for j in range(i+i,N+1,i):
            prime[j] = False

prime = [i for i in range(2,N+1) if prime[i] == True]


# 투포인터
start = 0
end = 0
sum = 0
ans = 0
while True:
    if sum == N:
        sum -= prime[start]
        start += 1
        ans += 1
    elif sum > N:
        sum -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        sum += prime[end]
        end += 1


print(ans)
    
