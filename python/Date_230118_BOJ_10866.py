# BOJ 10866
class Deque:
    def __init__(self):
        self.items = []	
    def push_front(self, val):
        if len(self.items) != 0:
            temp = []
            for i in range(len(self.items)):
                temp.append(self.items[i])
            self.items[0] = val
            for j in range(len(self.items)-1):
                self.items[j+1] = temp[j]
            self.items.append(temp[len(temp)-1])
        else:
            self.items.append(val)

    def push_back(self,val):
        self.items.append(val)
    
    def pop_front(self):
        if len(self.items) != 0:
            temp2 = self.items[0]
            for i in range(len(self.items)-1):
                self.items[i] = self.items[i+1]
            del self.items[-1]
            return print(temp2)
        else:
            print(-1)
    def pop_back(self):
        if len(self.items) != 0:

            temp = self.items[-1]
            del self.items[-1]
            return print(temp)
        else:
            print(-1)
    def size(self):	
        return print(len(self.items))
    def empty(self):
        if len(self.items) == 0:
            return print(1)
        else:
            return print(0)
    
    def front(self):
        if len(self.items) != 0:
            return print(self.items[0]) 
        else:
            return print(-1)
    def back(self):
        if len(self.items) != 0:
            return print(self.items[-1]) 
        else:
            return print(-1)
    


c = Deque()

from sys import stdin

n = int(stdin.readline())
for i in range(n):
    user_input = stdin.readline().split()
    if 'push_front' == user_input[0]:
        c.push_front(int(user_input[1]))
    elif 'push_back' == user_input[0]:
        c.push_back(int(user_input[1]))
    else:
        if user_input[0] =='size' : 
            c.size()
        elif user_input[0] == 'pop_back' : 
            c.pop_back()
        elif user_input[0] == 'pop_front':
            c.pop_front()
        elif user_input[0] == 'back': 
            c.back()
        elif user_input[0] == 'empty': 
            c.empty()
        elif user_input[0] == 'front': 
            c.front()
