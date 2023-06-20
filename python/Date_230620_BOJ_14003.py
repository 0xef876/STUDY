n = int(input())
data = list(map(int, input().split()))

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


dp = [0]
ans = []
for i in range(len(data)):
    if dp[-1] < data[i]:
        dp.append(data[i])
        ans.append((len(dp)-1, data[i]))
    else:
        idx = binary_search(dp, data[i])
        dp[idx] = data[i]
        ans.append((idx, data[i]))

temp = len(dp)-1
answer = []
for i in range(len(ans)-1, -1, -1):
    if ans[i][0] == temp:
        answer.append(ans[i][1])
        temp -= 1
answer.reverse()
print(len(answer))
print(*answer)
