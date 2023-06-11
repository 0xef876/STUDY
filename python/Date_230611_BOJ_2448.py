a = int(input())

star = [[" ", " ", "*", " ", " "], [" ", "*"," ", "*", " "], ["*", "*", "*", "*", "*"]]

def r(n,before):
    after = [[" "] * (2*2*n-1) for _ in range(2 * n)]
    for i in range(n):
        after[i][n:n+2*n-1] = before[i]
    
    k = 0
    for i in range(n,2*n):
        after[i][:2*n] = before[k]
        after[i][2*n:2*n+len(before[k])] = before[k]
        k+=1
    
    if 2*n == a:
        return after

    return r(2*n,after)

if a == 3:
    result = star
else:
    result = r(3,star)

for i in result:
    print("".join(i))
