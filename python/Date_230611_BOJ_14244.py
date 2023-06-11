n,m = map(int,input().split())

# n개의 노드
# m개의 리프로 이루어져 있는 트리
# 자식이 한개인 노드가 리프노드

# 예시 4 , 2 라면

#           0
#       1
#    2
# 3 

# 예시 4, 3 이라면
#        0
#    1 
# 2    3

# 예시 3, 2 라면
#        0
#    1
# 2 

# 예시 5, 3 이라면
#        0
#    1      
# 2    3
#        4

leaf = 0
if m==2:
    leaf = 1 # root노드를 리프로 설정

last_leaf = 0
for i in range(1,n):
    if m > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i
