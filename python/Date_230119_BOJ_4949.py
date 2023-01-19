# 4949
import sys,re
def check(s):
    stack = []
    for temp in s:
        if temp in '([':
            stack.append(temp)
        elif temp in ')]':
            if stack:
                temp_pop = stack.pop()
                if temp_pop == '(' and temp == ']':
                    return print("no")
                elif temp_pop == '[' and temp == ')': 
                    return print("no")
            else:
                return print("no")

    if len(stack) == 0:
        return print("yes")
    else:
        return print("no")
while True:
    state = True
    s = sys.stdin.readline()
    if len(s) == 2 and "." in s:
        break
    check(s)
