# 마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 주면 문제에서 원하는 답을 얻을 수 있다.

s = input().split('-')
ans = 0
for i in s[0].split('+'):
    ans += int(i)

for i in s[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)