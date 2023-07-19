a = int(input())
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
for _ in range(a):
    b = list(map(int, input().split()))
    c = b[1:]
    d = 0
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            d += gcd(c[i], c[j])
    print(d)