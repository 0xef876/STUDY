import sys
n = int(sys.stdin.readline().rstrip())

a = 0
b = 1
for i in range(n):
    a,b = (a+b) % (10 ** 9 +7),a % (10 ** 9 +7)
print(a)
