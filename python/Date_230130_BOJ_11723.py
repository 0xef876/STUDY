# BOJ 11723
import sys
n = int(sys.stdin.readline().rstrip())
class C:
    def __init__(self):
        self.S = set()
        self.count = 0
    def add(self,val):
        if val not in self.S:
            self.S.add(val)
            self.count += 1
    def remove(self,val):
        if val not in self.S:
            return
        else:
            self.S.remove(val)
            self.count += 1
    def check(self,val):
        if val in self.S:
            return 1
        else:
            return 0
    def toggle(self,val):
        if val in self.S:
            self.S.remove(val)
        else:
            self.S.add(val)
        
    def all(self):
        self.S = {1,2,3,4,5,6,7,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

    def empty(self):
        self.S = set()

test = C()

for i in range(n):
    user_input = sys.stdin.readline().rstrip()
    if ' ' in user_input:
        menu = user_input.split(' ')
        val = int(menu[1])
        if menu[0] == 'add':
            test.add(val)
        elif menu[0] == 'check':
            print(test.check(val))
        elif menu[0] == 'toggle':
            test.toggle(val)
        elif menu[0] == 'remove':
            test.remove(val)
    else:
        if user_input == 'all':
            test.all()
        elif user_input == 'empty':
            test.empty()
