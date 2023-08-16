def func(x,y,n):
    global answer
    first = arr[y][x]
    
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j]!=first:
                for k in range(3):
                   for l in range(3):
                       func(x+k*n//3,y+l*n//3,n//3)
                return
    
    answer[str(first)] +=1
    return
    

if __name__ == "__main__":
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    answer={"0":0,"1":0,"-1":0}   
    func(0,0,n)
    print(answer["-1"])
    print(answer["0"])
    print(answer["1"])
        

