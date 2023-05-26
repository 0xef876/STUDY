n = int(input())

martix = []
for i in range(n):
    data = list(map(int, input().split()))
    martix.append(data)

white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    color = martix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != martix[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0, 0, n)
print(white)
print(blue)
