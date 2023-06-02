N ,M = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
def backtracking(data,visited):
	if len(visited) == M:
		print(*visited)
		return
	for i in range(len(data)):
		if data[i] in visited:
			continue
		visited.append(data[i])
		backtracking(data,visited)
		visited.pop()

backtracking(data,[])
