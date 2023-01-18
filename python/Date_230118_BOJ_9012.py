# 9012
n = int(input())
for i in range(n):
    state = True
    dict = {'(':0,')':0}
    s = input()
    for j in s:
        dict[j] += 1
        if dict['('] < dict[')']:
            print("NO")
            state = False
            break
    if state :
        if dict['('] != dict[')']:
            print("NO")
        else:
            print("YES")
