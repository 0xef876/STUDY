import sys

# 입력 받기
N = int(sys.stdin.readline())

# 이진 탐색을 사용하여 정수 N의 제곱근 구하기
start = 1
end = N

while start <= end:
    mid = (start + end) // 2
    
    if mid ** 2 == N:
        print(mid)
        break
    elif mid ** 2 < N:
        start = mid + 1
    else:
        end = mid - 1
