N ,M = map(int,input().split())
data = list(map(int,input().split()))
tmp = [False] * N
ans = set()
def backtracking(data,visited,tmp):
	if len(visited) == M:
		# visited가 오름차순이 아니면 return
		for i in range(len(visited)-1):
			if visited[i] > visited[i+1]:
				return 
		ans.add(tuple(visited))
		return 
	for i in range(len(data)):
		if data[i] in visited and tmp[i] == True:
			continue 
		visited.append(data[i])
		tmp[i] = True
		backtracking(data,visited,tmp)
		tmp[i] = False
		visited.pop()


backtracking(data,[],tmp)

for i in sorted(ans):
	print(*i)
