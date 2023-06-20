l,c = map(int,input().split())
data = list(input().split())
data.sort()
vowel = ['a','e','i','o','u']
ans = []

def dfs(idx, cnt):
    if cnt == l:
        vowel_cnt = 0
        for i in ans:
            if i in vowel:
                vowel_cnt += 1
        if vowel_cnt >= 1 and vowel_cnt <= l-2:
            print(''.join(ans))
        return
    for i in range(idx,c):
        ans.append(data[i])
        dfs(i+1, cnt+1)
        ans.pop()

dfs(0,0)

