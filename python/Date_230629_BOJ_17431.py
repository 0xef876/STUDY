def solve(s):
    if ">" in s:
        s2 = s.split(">")
        # print("s2 = ",s2)
        for i in s2:
            if "<" in i:
                if i[0] == "<":
                    print(i+">",end="")
                else:
                    t = i.split("<")
                    if " " in t[0]:
                        t2 = t[0].split(" ")
                        for i in range(len(t2)):
                            print(t2[i][::-1],end="")
                            if i != len(t2)-1:
                                print(" ",end="")
                        print("<",end="")
                        print(t[1]+'>',end="")
                    else:
                        t[0] = t[0][::-1]
                        print(t[0],end="")
                        print("<",end="")
                        print(t[1]+'>',end="")
            elif " " in i:
                t = i.split(" ")
                for i in range(len(t)):
                    print(t[i][::-1],end="")
                    if i != len(t)-1:
                        print(" ",end="")
            else:
                print(i[::-1],end="")
    elif " " in s:
        s2 = s.split(" ")
        for i in range(len(s2)):
            print(s2[i][::-1],end="")
            if i != len(s2)-1:
                print(" ",end="")
    else:
        print(s[::-1],end="")
temp = input()
solve(temp)