# BOJ 1359
from sys import stdin as r
import math
n,m,k = map(int,r.readline().split())
확률 = 0
# 전체 경우
total = math.comb(n,m)
while m>=k:
    if n-m < m-k:
        k += 1
        continue
    확률 += (math.comb(m,k) * math.comb(n-m,m-k) / total)
    k += 1
print(확률)


