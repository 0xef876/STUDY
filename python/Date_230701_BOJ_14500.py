n,m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))


# 1. ㅡ 모양
# 2. ㅣ 모양
# 3. ㅁ 모양

# 4.
"""
o
o
oo
"""
# 5. 
"""
 o
 o
oo
"""
# 6.
"""
o o o
o
"""
# 7 .
""" 
o o o
    o
"""

# 8.
"""
    o
o o o
"""

# 9.
"""
o
o o o 
"""

# 10.
"""
oo
o
o
"""

# 11.
"""
oo
 o
 o
"""



# 12. ㅗ 모양
# 13. ㅜ 모양
# 14. ㅓ 모양
# 15. ㅏ 모양

# 16. ⚡️ 모양
# 17. ⚡️ 대칭 모양
# 18. ㅡ_ 모양
# 19. _ㅡ 모양

ans = 0
for i in range(n):
    for j in range(m):
        try : 
            # 1. ㅡ 모양
            temp1 = sum(data[i][j:j+4])
            if ans < temp1:
                ans = temp1
        except:
            pass

        try:
            # 2. ㅣ 모양
            temp2 = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
            if ans < temp2:
                ans = temp2
        except :
            pass
        try:
            # 3. ㅁ 모양
            temp3 =sum(data[i][j:j+2]) + sum(data[i+1][j:j+2])
            if ans < temp3:
                ans = temp3
        except :
            pass
        try:
            # 4.
            """
            o
            o
            oo
            """
            temp4 = data[i][j] + data[i+1][j] + sum(data[i+2][j:j+2])
            if ans < temp4:
                ans = temp4
        except :
            pass
        try:
            # 5. 
            """
             o
             o
            oo
            """
            temp5 = data[i][j+1] + data[i+1][j+1] + sum(data[i+2][j:j+2])
            if ans < temp5:
                ans = temp5
        except :
            pass

        
        try:
            # 6.
            """
            o o o
            o
            """
            
            temp6 = sum(data[i][j:j+3]) + data[i+1][j]
            if ans < temp6:
                ans = temp6
        except:
            pass
        
        try :
            # 7 .
            """ 
            o o o
                o
            """            
            temp7 = sum(data[i][j:j+3]) + data[i+1][j+2]
            if ans < temp7:
                ans = temp7
        except:
            pass
        try:
                
            # 8.
            """
                o
            o o o
            """
            temp8 = sum(data[i+1][j:j+3]) + data[i][j+2]
            if ans < temp8:
                ans = temp8
        except:
            pass
        try:
            # 9.
            """
            o
            o o o 
            """
            temp9 = sum(data[i+1][j:j+3]) + data[i][j]
            if ans < temp9:
                ans = temp9
        except:
            pass
        
        try : 
            # 10
            """
            oo
             o
             o
            """
            temp10 = sum(data[i][j:j+2]) + data[i+1][j+1] + data[i+2][j+1]
            if ans < temp10:
                ans = temp10
        except:
            pass

        try:
            # 11
            """
            oo
            o
            o
            """
            temp11 = sum(data[i][j:j+2]) + data[i+1][j] + data[i+2][j]
            if ans < temp11:
                ans = temp11
        except:
            pass

        try:
            # 12. ㅗ 모양
            temp12 = sum(data[i+1][j:j+3]) + data[i][j+1]
            if ans < temp12:
                ans = temp12
        except:
            pass
        try:
            # 13. ㅜ 모양
            temp13 = sum(data[i][j:j+3]) + data[i+1][j+1]
            if ans < temp13:
                ans = temp13
        except:
            pass
        try:
            # 14. ㅓ 모양
            temp14 = data[i][j+1] + data[i+1][j] + data[i+1][j+1] + data[i+2][j+1]
            if ans < temp14:
                ans = temp14
        except:
            pass
        try:
            # 15. ㅏ 모양
            temp15 = data[i][j] + data[i+1][j] + data[i+1][j+1] + data[i+2][j]
            if ans < temp15:
                ans = temp15
        except:
            pass
        try:
            # 16. ⚡️ 모양
            temp16 =  data[i][j] + sum(data[i+1][j:j+2]) + data[i+2][j+1]
            if ans < temp16:
                ans = temp16
        except:
            pass
        try:
            # 17. ⚡️  대칭모양
            temp17 = data[i][j+1] + sum(data[i+1][j:j+2]) + data[i+2][j]
            if ans < temp17:
                ans = temp17
        except:
            pass
        try:
            # 18. _ㅡ 모양
            temp18 = sum(data[i][j+1:j+3]) + sum(data[i+1][j:j+2])
            if ans < temp18:
                ans = temp18
        except:
            pass

        try:
            # 19. ㅡ_ 모양
            temp19 = sum(data[i][j:j+2]) + sum(data[i+1][j+1:j+3])
            if ans < temp19:
                ans = temp19
        except:
            pass

print(ans)