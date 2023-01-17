
# BOJ 10828
class Stack:
    def __init__(self):
        self.items = []	
    def push(self, val):
        self.items.append(val)
    def deque(self):
        try :
            num = self.items.pop()
            return print(num)
        except:
            print(-1)
    def top(self):
        try:
            return print(self.items[-1])  
        except IndexError:
            print(-1)

    def size(self):	
        return print(len(self.items))

    def empty(self):
        if len(self.items) == 0:
            return print(1)
        else:
            return print(0)

c = Stack()

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
        elif user_input[0] == 'empty': 
            c.empty()
        elif user_input[0] == 'top': 
            c.top()
