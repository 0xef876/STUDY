# 1735
def gcd(x, y):
    while x % y != 0:
        m = x % y
        x = y
        y = m
    return y
import sys
a, b = map(int,sys.stdin.readline().split())
c, d = map(int,sys.stdin.readline().split())

num = gcd(b,d)
ja = b * d // num
mo = a * (d // num) + c * (b // num)

num2 = gcd(ja,mo)

print(mo // num2 , ja // num2)
