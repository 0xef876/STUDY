n = input()
ans = 0


real_n = n
while True:
    if len(n) == 1:
        n = '0' + n
    temp = str(int(n[0]) + int(n[-1]))
    temp = temp[-1]
    n = n[-1] + temp[-1]
    ans += 1
    if int(n) == int(real_n):
        break

print(ans)
