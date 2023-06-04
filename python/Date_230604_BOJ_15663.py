N ,M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
tmp = [False] * N
ans = set()
def backtracking(data,visited,tmp):
	if len(visited) == M:
		ans.add(tuple(visited))
		return 
	for i in range(len(data)):
		if tmp[i]:
			continue
		visited.append(data[i])
		tmp[i] = True
		backtracking(data,visited,tmp)
		tmp[i] = False
		visited.pop()


backtracking(data,[],tmp)

for i in sorted(ans):
	print(*i)
