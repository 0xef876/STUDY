# BOJ 11047
import sys
n,k = map(int,sys.stdin.readline().split())
coin = []
count = 0
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip())) 
m = k
for i in range(len(coin)-1,-1,-1):
    if coin[i] > m:
        continue
    else:
        while k > 0:
            k -= coin[i]
            count += 1
        if k == 0:
            print(count)
            break
        else:
            k += coin[i]
            count -= 1
    
