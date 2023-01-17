# BOJ 10845
class Queue:
    def __init__(self):
        self.items = []	
        self.idx = 0
    def push(self, val):
        self.items.append(val)

    def deque(self):
        if len(self.items) == 0 or self.idx == len(self.items):
            return print(-1)
        else :
            x = self.items[self.idx]
            self.idx += 1
            return print(x)

    def front(self):
        try:
            return print(self.items[self.idx])  
        except IndexError:
            print(-1)

    def size(self):	
        return print(len(self.items) - self.idx)

    def back(self):
        if len(self.items) >= self.idx + 1:
            return print(self.items[-1]) 
        else:
            return print(-1)
    
    def empty(self):
        if len(self.items) - self.idx == 0:
            return print(1)
        else:
            return print(0)

c = Queue()

from sys import stdin

n = int(stdin.readline())
for i in range(n):
    user_input = stdin.readline().split()
    if 'push' == user_input[0]:
        c.push(int(user_input[1]))
    else:
        if user_input[0] =='size' : 
            c.size()
        elif user_input[0] == 'pop' : 
            c.deque()
        elif user_input[0] == 'back': 
            c.back()
        elif user_input[0] == 'empty': 
            c.empty()
        elif user_input[0] == 'front': 
            c.front()
