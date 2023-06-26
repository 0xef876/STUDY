N = int(input())
data = list(map(int,input().split()))
# 오큰수
stack = []
ans = [-1] * N
for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        ans[stack.pop()] = data[i]
    stack.append(i)
print(*ans)