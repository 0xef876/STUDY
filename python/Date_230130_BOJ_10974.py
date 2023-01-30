#BOJ 10974
import sys,itertools

def solve(n):
	arr = [i for i in range(1,n+1)]
	for i in list(itertools.permutations(arr, n)):
		for j in i:
			print(j,end=' ')
		print()

num = int(sys.stdin.readline().rstrip())
solve(num)
