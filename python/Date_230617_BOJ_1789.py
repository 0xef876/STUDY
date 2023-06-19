n = int(input())


start = 1
ans = 0
while True:
    ans += start
    if ans > n:
        print(start-1)
        break
    start += 1