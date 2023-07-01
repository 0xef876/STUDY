import sys
input = sys.stdin.readline

data = [tuple(map(int, input().split())) for _ in range(3)]


p1,p2,p3 = data[0],data[1],data[2]
x = (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) # x^2
y = (p2[0]-p3[0])*(p2[0]-p3[0]) + (p2[1]-p3[1])*(p2[1]-p3[1]) # y^2
z = (p3[0]-p1[0])*(p3[0]-p1[0]) + (p3[1]-p1[1])*(p3[1]-p1[1]) # z^2
# 기울기가 0 이면 X
if (p1[0]-p2[0]) * (p2[1]-p3[1]) == (p2[0]-p3[0]) * (p1[1]-p2[1]):
    print("X")
# 기울기가 0이 아니면
else:
    if 2 * max(x,y,z) == x + y + z:
        # 직각삼각형
        # 두변의 길이가 같으면
        if x == y or y == z or z == x:
            print("Jikkak2Triangle")
        # 세변의 길이가 모두 다르면
        else:
            print("JikkakTriangle")

    elif max(x,y,z) < x + y + z - max(x,y,z):
        # 예각삼각형
        # 세변의 길이가 같으면
        if x == y and y == z:
            print("JungTriangle")
        # 두변의 길이가 같으면
        elif x == y or y == z or z == x:
            print("Yeahkak2Triangle")
        # 세변의 길이가 모두 다르면
        else:
            print("YeahkakTriangle")

    elif max(x,y,z) > x + y + z - max(x,y,z):
        # 둔각삼각형
        # 두변의 길이가 같으면
        if x == y or y == z or z == x:
            print("Dunkak2Triangle")
        # 세변의 길이가 모두 다르면
        else:
            print("DunkakTriangle")