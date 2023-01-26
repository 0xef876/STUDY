# BOJ 1676
import sys
def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res
n = int(sys.stdin.readline().strip())

s = str(factorial(n))
count = 0
start = False
for i in range(-1,-1 * len(s),-1):
    if s[i] == '0':
        count += 1
        start = True
    elif start and s[i] != '0':
        print(count)
        start = False
        break
if count == 0:
    print(0)
