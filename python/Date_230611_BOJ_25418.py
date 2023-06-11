a,b = map(int,input().split())
cnt = 0

while True:
    if a == b:
        print(cnt)
        break
    if b % 2 == 0 and b >= a*2:
        b //= 2
    else:
        b -= 1
    cnt += 1
