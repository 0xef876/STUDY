import sys
n = int(sys.stdin.readline().rstrip())

f0 = 0
f1 = 1
f2 = 1
if n == 0 :
    print(f0)
elif n == 1:
    print(f1)
elif n == 2:
    print(f2)
else:
    for i in range(n-2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    print(f3)
