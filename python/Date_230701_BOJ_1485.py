import sys
input = sys.stdin.readline

a = int(input())
def dist(a,b):
    return abs(a[0]-b[0]) ** 2 + abs(a[1]-b[1]) ** 2
def check(arr):
    tmp = 0
    # arr을 x와 y 기준으로 정렬
    arr.sort(key=lambda x: (x[0], x[1]))

    for i in arr:
        if i == [0,0]:
            tmp += 1
    if tmp == 4:
        return 0
    
    elif dist(arr[0], arr[1]) == dist(arr[0], arr[2]) == dist(arr[1], arr[3]) and dist(arr[0], arr[3]) == dist(arr[1], arr[2]):
        return 1
    else:
        return 0
    
for i in range(a):
    print(check([list(map(int, input().split())) for _ in range(4)]))
