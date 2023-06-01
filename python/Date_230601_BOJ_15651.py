N ,M = map(int,input().split())
data = [i for i in range(1,N+1)]

def backtracking(data,visited):
	if len(visited) == M:
		print(*visited)
		return
	for i in range(len(data)):
		visited.append(data[i])
		backtracking(data,visited)
		visited.pop()

backtracking(data,[])
