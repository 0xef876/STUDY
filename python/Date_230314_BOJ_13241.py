def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
    
def lcm(a,b):
    return (a*b) // gcd(a,b)
    
x,y = map(int,input().split())
print(lcm(x,y))
