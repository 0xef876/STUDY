n = int(input())
k = int(input())

left, right = 1, n * n

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt < k:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
