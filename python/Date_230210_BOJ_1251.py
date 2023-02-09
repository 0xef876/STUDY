import sys
from itertools import permutations, combinations_with_replacement

n = sys.stdin.readline().rstrip()
temp_n = n
length = len(n)
def p(n,m):  # 자연수 분할 알고리즘
    A=[list(x) for x in combinations_with_replacement(range(1, n), m)  if sum(x)==n]
    return A



data = p(length,3)
result = []
for i in data:
    printList = set(permutations(i, 3))
    printList = list(printList)
    for j in range(len(printList)):
        printList[j] = list(printList[j])
    result.append(printList)
# print(result)
for i in range(len(result)):
    for j in range(len(result[i])):
        n = temp_n
        for k in range(3):
            temp = result[i][j][k]
            result[i][j][k] = n[0:result[i][j][k]]
            n = n[temp:]

ans = []
for i in result:
    for j in i:
        s = ''
        for k in j:
            s += k[::-1]
        ans.append(s)
ans.sort()
print(ans[0])
